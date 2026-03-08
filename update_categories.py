#!/usr/bin/env python3
"""
批量修改博客文章的 categories 字段
"""

import os
import re
from pathlib import Path

# 分类映射：文件夹路径 -> [父分类, 子分类]
CATEGORY_MAP = {
    '编程语言/Golang': ['编程语言', 'Golang'],
    '编程语言/Python': ['编程语言', 'Python'],
    '编程语言/C++': ['编程语言', 'C++'],
    '编程语言/前端': ['编程语言', '前端'],
    '算法/LeetCode': ['算法', 'LeetCode'],
    '算法/代码随想录': ['算法', '代码随想录'],
    '算法/速刷记录': ['算法', '速刷记录'],
    '技术栈/Docker': ['技术栈', 'Docker'],
    '技术栈/Git': ['技术栈', 'Git'],
    '技术栈/Linux': ['技术栈', 'Linux'],
    '技术栈/网络': ['技术栈', '网络'],
    '架构设计/架构': ['架构设计', '架构'],
    '架构设计/设计模式': ['架构设计', '设计模式'],
    'AI': ['AI'],
    '综合/工具': ['综合', '工具'],
    '综合/比赛': ['综合', '比赛'],
    '综合/极客时间': ['综合', '极客时间'],
}

def update_categories(file_path, categories):
    """更新文章的 categories 字段"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成新的 categories 内容
    if len(categories) == 1:
        new_categories = f"categories: {categories[0]}"
    else:
        new_categories = f"categories:\n  - [{categories[0]}, {categories[1]}]"
    
    # 匹配 categories 字段（支持多种格式）
    # 格式1: categories: xxx
    # 格式2: categories:\n  - xxx
    # 格式3: categories:\n  - [xxx, yyy]
    patterns = [
        r'categories:\s*\n\s*-\s*\[[^\]]+\]',  # categories:\n  - [xxx, yyy]
        r'categories:\s*\n\s*-\s+\S+',          # categories:\n  - xxx
        r'categories:\s*\S+',                    # categories: xxx
    ]
    
    for pattern in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, new_categories, content)
            break
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    posts_dir = Path('/root/.openclaw/workspace/blog-source/source/_posts')
    
    updated_count = 0
    
    for folder_path, categories in CATEGORY_MAP.items():
        folder = posts_dir / folder_path
        if not folder.exists():
            continue
        
        for md_file in folder.glob('*.md'):
            try:
                update_categories(md_file, categories)
                updated_count += 1
                print(f"✅ {md_file.name} -> {categories}")
            except Exception as e:
                print(f"❌ {md_file.name}: {e}")
    
    print(f"\n总计更新: {updated_count} 篇文章")

if __name__ == '__main__':
    main()