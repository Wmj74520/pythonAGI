# ============================================================
# 第 3 课：Prompt 怎么写（任务 / 角色 / 约束 / 示例）
#
# 运行：激活 .venv 后
#   .\.venv\Scripts\python.exe 第3课_Prompt写法.py
# ============================================================

import requests

API_KEY = "sk-把这里换成你自己的key"   
URL = "https://api.deepseek.com/chat/completions"


def ask(prompt):
    """把一句 prompt 发给 AI，返回它的回答"""
    resp = requests.post(
        URL,
        headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
        json={"model": "deepseek-flash", "messages": [{"role": "user", "content": prompt}]},
        timeout=30,
    )
    result = resp.json()
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    return "出错了：" + str(result)


# ---------- 1. 模糊提问：只说"做什么"，AI 自由发挥 ----------
print("=== 1. 模糊提问：介绍一下 Python ===")
print(ask("介绍一下 Python"))
print()


# ---------- 2. 清晰提问：任务 + 角色 + 约束 ----------
clear_prompt = """你是一位面向零基础学员的编程老师。
请用 3 句话介绍 Python，要求：
1. 每句话不超过 20 个字；
2. 不要用专业术语；
3. 结尾用一句鼓励的话。
"""
print("=== 2. 清晰提问（任务 + 角色 + 约束）===")
print(ask(clear_prompt))
print()


# ---------- 3. 带示例：给 1~2 个例子，它就会照着做 ----------
few_shot_prompt = """把下面的词翻译成英文，只输出译文，不要解释。
例子：
- 苹果 -> apple
- 香蕉 -> banana

请翻译：橘子
"""
print("=== 3. 带示例（few-shot）===")
print(ask(few_shot_prompt))
print()
