/**
 * 访客统计增量气泡
 * 在不蒜子数据加载后，计算并显示增量
 * 同一用户30分钟窗口内不更新baseline，以便看到累计增量
 *
 * v2.0 - 修复首次访问竞态条件：
 *   问题：不蒜子 async 加载慢时，JS 读到空值(0)就初始化了 baseline，
 *   下次访问显示整个历史量作为增量。
 *   修复：只有确认不蒜子真的返回了有效数据后才设置 baseline。
 */

(function() {
    var STORAGE_KEY = 'busuanzi_stats';
    var INIT_FLAG = 'busuanzi_initialized_ok'; // 专属初始化标记
    var TIME_WINDOW = 30 * 60 * 1000; // 30分钟（毫秒）

    function init() {
        // 给不蒜子留足时间加载，刷新也需要等缓存
        setTimeout(function() {
            updateStats();
        }, 2000);
    }

    /**
     * 读取存好的 baseline。
     * 如果还没初始化（第一次访问），返回 null 而不是空对象，
     * 以此通知 updateStats 继续等待不蒜子数据。
     */
    function getStoredStats() {
        try {
            var initialized = localStorage.getItem(INIT_FLAG);
            if (!initialized) {
                // 还没有初始化过，检查不蒜子数据是不是真的到了
                var uvEl = document.getElementById('busuanzi_value_site_uv');
                var pvEl = document.getElementById('busuanzi_value_site_pv');
                if (!uvEl || !pvEl) {
                    return null; // 元素都还没渲染，重试
                }

                var uvText = uvEl.textContent || '';
                var pvText = pvEl.textContent || '';

                // 不蒜子返回的数据不会为空，如果还是空或者 '0'，说明还没加载完
                if (!uvText || uvText === '0' || uvText === '' ||
                    !pvText || pvText === '0' || pvText === '') {
                    return null; // 不蒜子还没填充数据，继续等
                }

                // 不蒜子真的加载完了，用真实数据初始化 baseline
                var currentUV = parseInt(uvText) || 0;
                var currentPV = parseInt(pvText) || 0;

                if (currentUV <= 0 && currentPV <= 0) {
                    return null; // 数据异常，再等一轮
                }

                var stats = {
                    uv: currentUV,
                    pv: currentPV,
                    lastVisit: Date.now()
                };
                localStorage.setItem(STORAGE_KEY, JSON.stringify(stats));
                localStorage.setItem(INIT_FLAG, '1');
                console.log('[访客统计] 首次初始化baseline成功，UV:', currentUV, 'PV:', currentPV);
                return stats;
            }

            // 已经初始化过了，直接读取
            return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
        } catch(e) {
            return {};
        }
    }

    function saveStats(uv, pv) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
            uv: uv,
            pv: pv,
            lastVisit: Date.now()
        }));
    }

    function updateStats() {
        var uvEl = document.getElementById('busuanzi_value_site_uv');
        var pvEl = document.getElementById('busuanzi_value_site_pv');

        if (!uvEl || !pvEl) {
            setTimeout(updateStats, 1000);
            return;
        }

        var currentUV = parseInt(uvEl.textContent) || 0;
        var currentPV = parseInt(pvEl.textContent) || 0;

        // getStoredStats 返回 null 表示不蒜子还没准备好，重试
        var stored = getStoredStats();
        if (stored === null) {
            console.log('[访客统计] 等待不蒜子数据...');
            setTimeout(updateStats, 1000);
            return;
        }

        var lastUV = stored.uv || 0;
        var lastPV = stored.pv || 0;
        var lastVisit = stored.lastVisit || 0;

        // 首次访问（理论不会走到这里，因为 getStoredStats 里已经初始化了）
        // 但作为安全兜底
        if (!lastVisit) {
            saveStats(currentUV, currentPV);
            localStorage.setItem(INIT_FLAG, '1');
            console.log('[访客统计] 兜底初始化，UV:', currentUV, 'PV:', currentPV);
            return;
        }

        // 计算增量
        var uvIncrease = currentUV > lastUV ? currentUV - lastUV : 0;
        var pvIncrease = currentPV > lastPV ? currentPV - lastPV : 0;

        // 添加增量气泡
        if (uvIncrease > 0) {
            addBadge(uvEl, uvIncrease);
        }
        if (pvIncrease > 0) {
            addBadge(pvEl, pvIncrease);
        }

        // 只有超过30分钟才更新baseline（防止刷新重置）
        if ((Date.now() - lastVisit) >= TIME_WINDOW) {
            saveStats(currentUV, currentPV);
            console.log('[访客统计] 已更新baseline，UV:', currentUV, 'PV:', currentPV);
        } else {
            var remaining = Math.ceil((TIME_WINDOW - (Date.now() - lastVisit)) / 60000);
            console.log('[访客统计] 当前UV:', currentUV, '| PV:', currentPV, '| 显示增量 UV:+' + uvIncrease, 'PV:+' + pvIncrease, '| ' + remaining + '分钟后更新baseline');
        }
    }

    function addBadge(element, count) {
        var badge = document.createElement('span');
        badge.className = 'visitor-increase-badge';
        badge.textContent = '+' + formatNumber(count);
        badge.style.cssText = 'margin-left:8px;background:#ff4757;color:#fff;font-size:10px;padding:2px 6px;border-radius:10px;font-weight:600;vertical-align:middle;display:inline-block;';
        element.parentNode.style.position = 'relative';
        element.parentNode.appendChild(badge);
    }

    function formatNumber(n) {
        if (n >= 10000) {
            return (n / 10000).toFixed(1) + '万';
        }
        return n;
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    window.addEventListener('pjax:complete', function() {
        setTimeout(updateStats, 1500);
    });
})();
