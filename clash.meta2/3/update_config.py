import re

# 文件路径
config_file = "config.yaml"

# 读取文件内容
with open(config_file, "r") as file:
    content = file.read()

# 定义匹配并更新二级域名的函数
def increment_domain(match):
    prefix = match.group(1)  # 保留域名前缀（如 m）
    num = int(match.group(2)) + 1  # 数字加 1
    suffix = match.group(3)  # 保留域名后缀（如 .106778.xyz）
    return f"{prefix}{num}{suffix}"

# 更新 servername 和 Host 字段中的域名
updated_content = re.sub(r"(servername:\s+m)(\d+)(\.106778\.xyz)", increment_domain, content)
updated_content = re.sub(r"(Host:\s+m)(\d+)(\.106778\.xyz)", increment_domain, updated_content)

# 将更新后的内容写回文件
with open(config_file, "w") as file:
    file.write(updated_content)

print("更新完成：所有节点的二级域名已加 1。")
