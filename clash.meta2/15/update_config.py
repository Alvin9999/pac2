import re
import os

# 使用相对路径指向正确的目录
config_file = os.path.join(os.path.dirname(__file__), "config.yaml")

# 读取原始 config.yaml 文件
with open(config_file, "r") as file:
    content = file.read()

# 正则表达式匹配 servername 和 host 中的数字，并将其加 1
def increment_domain(match):
    base = match.group(1)
    num = int(match.group(2)) + 1  # 将数字加 1
    suffix = match.group(3)
    return f"{base}{num}{suffix}"

# 更新 servername 和 host
updated_content = re.sub(r"(servername:\s+m)(\d+)(\.164748\.xyz)", increment_domain, content)
updated_content = re.sub(r"(Host:\s+m)(\d+)(\.164748\.xyz)", increment_domain, updated_content)

# 将更新后的内容写回文件
with open(config_file, "w") as file:
    file.write(updated_content)

print("更新完成：所有节点的二级域名已加 1。")
