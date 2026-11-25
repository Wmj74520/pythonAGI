# ============================================================
# 第 2 课：对话角色 system / user / assistant
#
# 运行：激活 .venv 后，用
#   .\.venv\Scripts\python.exe 第2课_对话角色.py
# ============================================================

import requests

API_KEY = "sk-把这里换成你自己的key"  
URL = "https://api.deepseek.com/chat/completions"

def ask(messages):
    resp = requests.post(
        URL,
        headers = {"Authorization": "Bearer " + API_KEY,"Content-Type": "application/json"},
        json = {"model": "deepseek-flash", "messages":messages},
        timeout=30,
    )
    result = resp.json()
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return "错了:" + str(result)

messages =[
    {"role":"system","content":"你是一个说话简短的老师，每次回答不超错2句话"},
]

messages.append({"role":"user","content":"请问什么是python？"})
answer1 = ask(messages)
print("问：什么是python?")
print("答：",answer1)
print()

messages.append({"role":"assistant","content":"answer1"})

messages.append({"role":"user","content":"请问它能干什么?"})
answer2 = ask(messages)
print("问：它能干什么?")
print("答:",answer2)

print("\n")

print("messages现在一共有",len(messages),"条消息")
for m in messages:
    print(" -", m["role"],":", m["content"][:30])