/**
 * 访客统计增量气泡
 * 在不蒜子数据加载后，计算并显示增量
 * 同一用户30分钟窗口内不更新baseline，以便看到累计增量
 */

(function() {
    var STORAGE_KEY = 'busuanzi_stats';
    var TIME_WINDOW = 30 * 60 * 1000; // 30分钟（毫秒）

    function init() {
        setTimeout(function() {
            updateStats();
        }, 1500);
    }

    function getStoredStats() {
        try {
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

        var stored = getStoredStats();
        var lastUV = stored.uv || 0;
        var lastPV = stored.pv || 0;
        var lastVisit = stored.lastVisit || 0;

        // 计算增量（始终显示，只要当前 > 存储值）
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
        if (!lastVisit || (Date.now() - lastVisit) >= TIME_WINDOW) {
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