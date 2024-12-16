import re
import os
import json

# 指定 config.json 文件路径
config_file = os.path.join(os.path.dirname(__file__), "config.json")

# 检查文件是否存在
if not os.path.exists(config_file):
    raise FileNotFoundError(f"{config_file} 不存在，请检查路径。")

# 读取 config.json 文件
with open(config_file, "r", encoding="utf-8") as file:
    content = file.read()

# 定义更新二级域名的函数
def increment_domain(match):
    base = match.group(1)
    num = int(match.group(2)) + 1  # 将数字加 1
    suffix = match.group(3)
    return f"{base}{num}{suffix}"

# 正则表达式匹配并替换域名中的数字
updated_content = re.sub(r"(a)(\d+)(\.164748\.xyz)", increment_domain, content)

# 将更新后的内容写回 config.json
with open(config_file, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("更新完成：所有二级域名已加 1。")
