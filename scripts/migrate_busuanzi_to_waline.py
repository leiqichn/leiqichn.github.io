#!/usr/bin/env python3
"""
不蒜子数据迁移到Waline脚本
功能：将busuanzi的访问量数据导入Waline的wl_Counter表

使用方法：
1. 在浏览器访问你的博客
2. 打开开发者工具 -> Network -> 找busuanzi请求
3. 或使用下方数据格式手动输入
"""

import sqlite3
import json
from datetime import datetime

# Waline数据库路径
WALINE_DB = "/var/www/waline/data/waline.sqlite"

# 不蒜子数据（请替换为实际数据）
# 格式：{"页面路径": 访问次数}
# 可以从不蒜子网站或浏览器开发者工具获取
BUSUANZI_DATA = {
    # 示例数据，请替换为实际值
    # "/": 1000,           # 首页访问量
    # "/guestbook/": 500,   # 留言板
    # "/about/": 200,       # 关于页
    # 添加更多页面...
}

def migrate_busuanzi_to_waline(data, dry_run=True):
    """
    将不蒜子数据迁移到Waline
    
    Args:
        data: 不蒜子数据字典 {url: count}
        dry_run: True=只显示将要执行的操作，False=实际执行
    """
    conn = sqlite3.connect(WALINE_DB)
    cursor = conn.cursor()
    
    print("=" * 50)
    print("📊 不蒜子数据迁移到Waline")
    print("=" * 50)
    print()
    
    if dry_run:
        print("⚠️  试运行模式（不会实际修改数据）")
        print("   设置 dry_run=False 来执行实际迁移")
        print()
    
    results = []
    
    for url, count in data.items():
        # 检查是否已存在
        cursor.execute("SELECT time FROM wl_Counter WHERE url = ?", (url,))
        existing = cursor.fetchone()
        
        if existing:
            old_count = existing[0]
            action = "UPDATE"
            detail = f"{old_count} → {count} (+{count - old_count})"
        else:
            action = "INSERT"
            detail = f"新增 {count}"
        
        results.append({
            "url": url,
            "action": action,
            "count": count,
            "detail": detail
        })
        
        if not dry_run:
            if existing:
                cursor.execute("UPDATE wl_Counter SET time = ? WHERE url = ?", (count, url))
            else:
                cursor.execute("INSERT INTO wl_Counter (url, time) VALUES (?, ?)", (url, count))
    
    if not dry_run:
        conn.commit()
        print("✅ 迁移完成！")
        print()
    
    conn.close()
    
    # 打印结果
    print(f"{'页面路径':<50} {'操作':<10} {'访问量'}")
    print("-" * 80)
    for r in results:
        print(f"{r['url']:<50} {r['action']:<10} {r['detail']}")
    
    print()
    print(f"总计: {len(results)} 条记录")
    print(f"总访问量: {sum(r['count'] for r in results):,}")

def get_waline_stats():
    """获取Waline当前统计数据"""
    conn = sqlite3.connect(WALINE_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT url, time FROM wl_Counter ORDER BY time DESC")
    rows = cursor.fetchall()
    
    print("\n📊 Waline当前统计数据:")
    print("-" * 50)
    for url, time in rows:
        print(f"  {url}: {time:,}")
    
    print(f"\n总计: {len(rows)} 条记录, {sum(r[1] for r in rows):,} 次访问")
    
    conn.close()

def export_to_json(filename="busuanzi_export.json"):
    """导出当前Waline数据为JSON"""
    conn = sqlite3.connect(WALINE_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT url, time FROM wl_Counter")
    rows = cursor.fetchall()
    
    data = {url: time for url, time in rows}
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已导出到 {filename}")
    conn.close()

if __name__ == "__main__":
    import sys
    
    print("\n" + "=" * 50)
    print("不蒜子 → Waline 数据迁移工具")
    print("=" * 50)
    
    # 显示Waline当前数据
    get_waline_stats()
    
    print("\n" + "=" * 50)
    print("迁移说明:")
    print("=" * 50)
    print("""
1. 获取不蒜子数据方法：
   - 访问 https://busuanzi.ibruce.info
   - 或在博客页面打开浏览器开发者工具
   - Network -> 筛选 busuanzi -> 查看响应

2. 编辑本脚本中的 BUSUANZI_DATA 变量
   - 填入实际的不蒜子访问量数据

3. 运行迁移：
   python3 migrate_busuanzi_to_waline.py
    """)
    
    # 如果有数据则执行迁移
    if BUSUANZI_DATA:
        print("\n发现不蒜子数据，开始迁移...")
        # 先试运行
        migrate_busuanzi_to_waline(BUSUANZI_DATA, dry_run=True)
        
        print("\n⚠️  以上为预览，设置 dry_run=False 执行实际迁移")
    else:
        print("\n❌ 请先在脚本中填写 BUSUANZI_DATA 数据")
        print("   示例格式:")
        print('   BUSUANZI_DATA = {"/": 1000, "/guestbook/": 500}')
    
    # 导出当前数据
    print("\n")
    export_to_json()