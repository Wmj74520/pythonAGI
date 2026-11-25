# ============================================================
# 第 1 课：第一次让 AI 说话（调用 DeepSeek 大模型 API）
#
# 用法：
#   1. 把下面 API_KEY 换成你自己的 key
#   2. 先激活小房间：  .\.venv\Scripts\Activate.ps1
#   3. 再运行：        python 第1课_第一次调用API.py
# ============================================================

import requests

API_KEY = "sk-把这里换成你自己的key"   # ← 只改这一行！

URL = "https://api.deepseek.com/chat/completions"

headers ={
    "Authorization":"Bearer "+ API_KEY,
    "Content-Type":"application/json"
}
data ={
    "model":"deepseek-flash",
    "messages":[
        {"role":"user","content":"用一句话解释什么是api"}
    ]
}
resp = requests.post(URL,headers=headers,json=data,timeout=30)
# 200=成功；401=key不对；402/余额不足=需要充值
print("HTTP 状态码:",resp.status_code)
result =resp.json()
print(result)
print("\n--- 我只要 AI 的回答 ---")
if "choices" in result:
    print("AI的回答:",result["choices"][0]["message"]["content"])
else:
    print("出错了:",result)
