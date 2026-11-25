# 第 1 课（附）：列出你账号里可用的模型
# 用法：激活 .venv 后，把 API_KEY 换成你的，运行
#   python 第1课_查看可用模型.py

import requests

API_KEY = "sk-把这里换成你自己的key" .strip()  # ← 改这一行

URL = "https://api.deepseek.com/models"

resp = requests.get(
    URL,
    headers={"Authorization": "Bearer " + API_KEY},
    timeout=30,
)

print("HTTP 状态码:", resp.status_code)

data = resp.json()
if resp.status_code != 200:
    print("出错了：", data)
else:
    print("\n你账号可用的模型 ID（把其中一个填进 model 即可）：")
    for m in data.get("data", []):
        print("  -", m["id"])
