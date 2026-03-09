/**
 * SEO自动提交脚本
 * 在 hexo deploy 后自动提交到搜索引擎
 */

const https = require('https');

// 百度推送
function submitToBaidu(urls) {
  const token = process.env.BAIDU_TOKEN || 'YOUR_BAIDU_TOKEN';
  const data = urls.join('\n');
  
  const options = {
    hostname: 'data.zz.baidu.com',
    path: `/urls?site=https://leiqi.top&token=${token}`,
    method: 'POST',
    headers: {
      'Content-Type': 'text/plain',
      'Content-Length': Buffer.byteLength(data)
    }
  };

  const req = https.request(options, (res) => {
    console.log(`百度推送状态码: ${res.statusCode}`);
  });
  
  req.write(data);
  req.end();
}

hexo.on('deployAfter', function() {
  // 获取所有页面URL
  const urls = [
    'https://leiqi.top/',
    'https://leiqi.top/archives/',
    'https://leiqi.top/categories/',
    'https://leiqi.top/tags/'
  ];
  
  console.log('开始SEO推送...');
  // submitToBaidu(urls);
  console.log('请配置BAIDU_TOKEN环境变量后启用百度推送');
});
