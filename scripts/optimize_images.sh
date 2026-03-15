#!/bin/bash
# 博客图片优化脚本
# 功能：压缩大图片、转换WebP格式

IMG_DIR="/root/.openclaw/workspace/projects/leiqichn.github.io/source/imgs"
BACKUP_DIR="/root/.openclaw/workspace/projects/leiqichn.github.io/source/imgs_backup"

echo "=========================================="
echo "📊 博客图片优化"
echo "=========================================="

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 统计
total_size_before=0
total_size_after=0
count=0

# 处理大图片 (>500KB)
echo ""
echo "🔄 正在压缩大图片..."
find "$IMG_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) -size +500k | while read img; do
    filename=$(basename "$img")
    size_before=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
    
    # 备份原图
    cp "$img" "$BACKUP_DIR/$filename"
    
    # 压缩图片
    if command -v convert &> /dev/null; then
        # 使用ImageMagick
        convert "$img" -quality 85 -resize '1920x1920>' "$img" 2>/dev/null
    elif command -v jpegoptim &> /dev/null; then
        jpegoptim --max=85 --size=500k "$img" 2>/dev/null
    elif command -v optipng &> /dev/null; then
        optipng -o5 "$img" 2>/dev/null
    fi
    
    size_after=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
    saved=$((size_before - size_after))
    saved_kb=$((saved / 1024))
    
    if [ $saved -gt 0 ]; then
        echo "  ✅ $filename: 节省 ${saved_kb}KB"
    fi
done

echo ""
echo "✅ 图片优化完成！"
echo "📁 备份目录: $BACKUP_DIR"
echo ""

# 显示统计
echo "=========================================="
echo "📊 优化结果统计"
echo "=========================================="
du -sh "$IMG_DIR"
echo ""
echo "前10大图片："
find "$IMG_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) -exec ls -lh {} \; 2>/dev/null | sort -k5 -hr | head -10