# ============================================================
# 第 4 课：让 AI 返回规整的 JSON（结构化输出 + JSON 校验）
#
# 运行：激活 .venv 后
#   .\.venv\Scripts\python.exe 第4课_结构化输出.py
# ============================================================

import json
import requests

API_KEY = "sk-把这里换成你自己的key"   
URL = "https://api.deepseek.com/chat/completions"


def ask(prompt, json_mode=False):
    """把 prompt 发给 AI，返回它的回答文字"""
    body={
        "model": "deepseek-flash",
        "messages": [{"role": "user", "content": prompt}],
    }
    if json_mode:
        body["response_format"] = {"type": "json_object"}

    resp = requests.post(
        URL,
        headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
        json=body,
        timeout=30,
    )
    result = resp.json()
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    return None


# ---------- 1. 让 AI 把一段文字整理成 JSON ----------
prompt = """把下面这段学习记录整理成 JSON，字段固定为：
- date：日期（字符串，格式 YYYY-MM-DD）
- topic：主题（字符串）
- difficulty：难度（数字 1-5）

只输出 JSON，不要任何解释，不要用代码块包裹。

学习记录：2026-11-22 今天学了 Python 的类和对象，感觉有点难，打 4 分。
"""

text = ask(prompt,json_mode=True)
print("=== AI 返回的原始文字 ===")
print(text)
print()


# ---------- 2. 解析（校验）：把文字变成 Python 字典 ----------
print("=== 解析成 Python 字典 ===")
try:
    data = json.loads(text)
    print("解析成功！")
    print("  日期：", data["date"])
    print("  主题：", data["topic"])
    print("  难度：", data["difficulty"])
except json.JSONDecodeError as e:
    print("解析失败：AI 返回的不是合法 JSON")
    print("  错误：", e)


# ---------- 3. 演示：AI「多嘴」会怎样 ----------
print("\n=== 演示：AI 多嘴会导致解析失败 ===")
bad_text = '好的，这是您要的 JSON：{"date": "2026-11-22"}'
print("AI 返回：", bad_text)
try:
    json.loads(bad_text)
    print("解析成功（不会走到这里）")
except json.JSONDecodeError:
    print("解析失败！因为前面多了「好的，这是您要的 JSON：」")
    print("→ 应对：① prompt 强调只输出 JSON；② 代码清洗；③ 用 response_format 强制")
