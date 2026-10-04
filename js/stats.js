// 自建统计服务
(function() {
    const page = window.location.pathname;
    
    // 发送访问记录
    fetch('/api/stats?action=ping&page=' + encodeURIComponent(page)).catch(() => {});
    
    // 获取并显示统计
    fetch('/api/stats?action=get&page=' + encodeURIComponent(page))
        .then(r => r.json())
        .then(data => {
            document.querySelectorAll('[data-site-uv]').forEach(el => {
                el.textContent = data.site_uv || 0;
            });
            document.querySelectorAll('[data-site-pv]').forEach(el => {
                el.textContent = data.site_pv || 0;
            });
            document.querySelectorAll('[data-page-pv]').forEach(el => {
                el.textContent = data.page_pv || 0;
            });
        });
})();
