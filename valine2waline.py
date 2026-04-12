#!/usr/bin/env python3
"""
Valine 到 Waline 评论数据转换脚本
将 Valine (LeanCloud) 导出的评论数据转换为 Waline 格式
"""

import json
import re
from datetime import datetime


# Valine 表情符号到 emoji 的映射表
EMOTION_MAP = {
    'whee': '😁',
    'no way': '😱',
    'clap': '👏',
    'amorousness': '😍',
    'longing': '🥺',
    'love you': '😘',
    'happy': '😊',
    'tear': '😢',
    'punch': '👊',
}


def convert_emotions_to_emoji(text):
    """
    将 Valine 的表情符号语法 :emotion: 转换为对应的 emoji
    """
    def replace_emotion(match):
        emotion_name = match.group(1).strip()
        return EMOTION_MAP.get(emotion_name, match.group(0))
    
    # 匹配 :xxx: 格式的表情符号，但排除 URL 中的冒号
    # 使用负向后顾断言确保冒号前不是 http 或 https
    return re.sub(r'(?<!https)(?<!http):([a-z\s]+):', replace_emotion, text)


def convert_valine_to_waline(valine_data):
    """
    将 Valine 格式的评论数据转换为 Waline 格式
    
    主要字段映射：
    - objectId: 保持不变，作为评论的唯一标识
    - comment: 评论内容，保持不变
    - nick: 昵称，保持不变
    - mail: 邮箱，保持不变
    - link: 网站链接，保持不变
    - ua: User Agent，保持不变
    - ip: IP地址，保持不变
    - url: 评论所在页面URL，保持不变
    - pid: 父评论ID，保持不变
    - rid: 根评论ID，保持不变
    - createdAt/updatedAt/insertedAt: 时间字段，保持不变
    
    新增字段（Waline特有）：
    - user_id: 用户ID，设为null（匿名用户）
    - status: 评论状态，默认为"approved"（已批准）
    - sticky: 置顶标记，设为null
    - like: 点赞数，设为null
    - QQAvatar: Valine特有字段，不转换到Waline
    """
    
    waline_comments = []
    
    for valine_comment in valine_data:
        # 转换评论内容中的表情符号
        original_comment = valine_comment.get("comment", "")
        converted_comment = convert_emotions_to_emoji(original_comment)
        
        waline_comment = {
            "user_id": None,
            "comment": converted_comment,
            "ip": valine_comment.get("ip", ""),
            "link": valine_comment.get("link", ""),
            "mail": valine_comment.get("mail", ""),
            "nick": valine_comment.get("nick", "Anonymous"),
            "pid": valine_comment.get("pid"),
            "rid": valine_comment.get("rid"),
            "sticky": None,
            "status": "approved",
            "like": None,
            "ua": valine_comment.get("ua", ""),
            "url": valine_comment.get("url", "/"),
            "objectId": valine_comment.get("objectId", ""),
            "insertedAt": valine_comment.get("insertedAt", valine_comment.get("createdAt")),
            "createdAt": valine_comment.get("createdAt"),
            "updatedAt": valine_comment.get("updatedAt", valine_comment.get("createdAt"))
        }
        
        waline_comments.append(waline_comment)
    
    return waline_comments


def create_waline_export(comments):
    """
    创建完整的 Waline 导出格式
    """
    return {
        "__version": "1.39.3",
        "type": "waline",
        "version": 1,
        "time": int(datetime.now().timestamp() * 1000),
        "tables": ["Comment", "Counter", "Users"],
        "data": {
            "Comment": comments,
            "Counter": [],
            "Users": []
        }
    }


def main():
    # 读取 Valine 数据
    with open('valine_Comment_20260315_121359.json', 'r', encoding='utf-8') as f:
        valine_data = json.load(f)
    
    print(f"读取到 {len(valine_data)} 条 Valine 评论")
    
    # 转换为 Waline 格式
    waline_comments = convert_valine_to_waline(valine_data)
    
    # 创建完整的导出数据
    waline_export = create_waline_export(waline_comments)
    
    # 保存为 JSON 文件
    output_path = 'waline_output.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(waline_export, f, ensure_ascii=False, indent=2)
    
    print(f"转换完成！已生成 {len(waline_comments)} 条 Waline 评论")
    print(f"输出文件：{output_path}")
    
    # 打印一些统计信息
    urls = set(comment['url'] for comment in waline_comments)
    print(f"\n统计信息：")
    print(f"- 总评论数：{len(waline_comments)}")
    print(f"- 涉及页面数：{len(urls)}")
    
    # 统计回复评论数量
    replies = [c for c in waline_comments if c['pid'] is not None]
    print(f"- 回复评论数：{len(replies)}")
    print(f"- 顶级评论数：{len(waline_comments) - len(replies)}")
    
    # 统计表情符号转换
    emotion_count = sum(1 for c in valine_data if any(f':{e}:' in c.get('comment', '') for e in EMOTION_MAP.keys()))
    print(f"- 包含表情符号的评论数：{emotion_count}")


if __name__ == "__main__":
    main()
