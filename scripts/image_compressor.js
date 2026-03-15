/**
 * Hexo 构建时图片压缩插件
 * 在 hexo generate 后压缩 public 目录中的图片
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

hexo.on('generateAfter', function() {
  const publicDir = hexo.public_dir;
  const imgsDir = path.join(publicDir, 'imgs');
  
  if (!fs.existsSync(imgsDir)) {
    return;
  }
  
  console.log('\n🖼️  开始压缩图片...\n');
  
  try {
    // 使用 Python 脚本压缩
    const scriptPath = path.join(hexo.base_dir, 'scripts', 'compress_images.py');
    
    if (fs.existsSync(scriptPath)) {
      execSync(`python3 "${scriptPath}" "${imgsDir}"`, { stdio: 'inherit' });
    } else {
      // 简单压缩：使用 Python PIL
      const code = `
import os
import sys
from PIL import Image

img_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
count = 0
saved = 0

for root, dirs, files in os.walk(img_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(root, f)
            try:
                size_before = os.path.getsize(path)
                img = Image.open(path)
                
                if f.lower().endswith('.png'):
                    img.save(path, 'PNG', optimize=True)
                else:
                    img.save(path, 'JPEG', quality=85, optimize=True)
                
                size_after = os.path.getsize(path)
                if size_before > size_after:
                    saved += size_before - size_after
                    count += 1
                    print(f'  ✅ {f}: {size_before//1024}KB → {size_after//1024}KB')
            except Exception as e:
                pass

print(f'\\n📊 压缩完成: {count}张图片, 节省 {saved//1024}KB')
`;
      execSync(`python3 -c '${code.replace(/'/g, "'\"'\"'")}' "${imgsDir}"`, { stdio: 'inherit' });
    }
  } catch (err) {
    console.log('⚠️  图片压缩跳过（需要安装 Pillow: pip install Pillow）');
  }
});