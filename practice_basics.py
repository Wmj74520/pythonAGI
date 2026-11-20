# -*- coding: utf-8 -*-
"""
Python 基础练习（面向 agent 开发）
重点：f-string、dict 操作、列表推导式、for 遍历元素

运行方式：在终端输入  python practice_basics.py
"""


def sep(title: str) -> None:
    """打印一个带标题的分隔线，方便看输出"""
    print("\n" + "=" * 50)
    print(f"### {title}")
    print("=" * 50)


# ============================================================
# 1. f-string（拼提示词 / 拼字符串）
# ============================================================
sep("1. f-string 字符串格式化")

name = "小明"
role = "客服助手"
city = "北京"

# 基本用法：花括号里放变量
print(f"你好，我是{name}")

# 拼 agent 的 system prompt（三引号 + f-string 是写长提示词的标配）
system_prompt = f"""你是{role}，负责回答用户问题。

规则：
1. 用中文回答
2. 不知道就说不知道，不要编造

用户来自：{city}
"""
print(system_prompt)

# 花括号里还能放表达式
a, b = 3, 4
print(f"{a} + {b} = {a + b}")

# 控制小数位数、千分位（格式化输出常用）
price = 12345.678
print(f"价格：{price:.2f}")          # 保留 2 位小数 -> 12345.68
print(f"价格：{price:,.2f}")         # 加千分位 -> 12,345.68


# ============================================================
# 2. dict 操作（agent 的工具参数、配置、状态全靠它）
# ============================================================
sep("2. dict 字典操作")

# 创建字典
tool_args = {"city": "北京", "days": 3, "mode": "自由行"}
print("原始字典：", tool_args)

# 取值
print("取 city：", tool_args["city"])            # 键不存在会报错 KeyError
print("取 days：", tool_args.get("days"))        # get 取值
print("取不存在的键：", tool_args.get("hotel"))  # 返回 None，不报错
print("取不存在的键给默认值：", tool_args.get("hotel", "未指定"))

# 增 / 改 / 删
tool_args["budget"] = 5000        # 新增
tool_args["days"] = 5             # 修改
del tool_args["mode"]             # 删除
print("增改删后：", tool_args)

# 判断键是否存在
if "budget" in tool_args:
    print("有 budget 这个键")

# 遍历字典（agent 里经常要遍历工具参数）
for key, value in tool_args.items():
    print(f"  {key} -> {value}")

# 只取键 / 只取值
print("所有键：", list(tool_args.keys()))
print("所有值：", list(tool_args.values()))

# 两个字典合并（Python 3.9+ 用 | 运算符）
default_args = {"language": "中文", "currency": "CNY"}
merged = default_args | tool_args     # 后面的覆盖前面的同名字段
print("合并后：", merged)


# ============================================================
# 3. 列表推导式（一行生成 / 过滤列表）
# ============================================================
sep("3. 列表推导式")

nums = [1, 2, 3, 4, 5, 6]

# 映射：每个元素平方
squares = [n * n for n in nums]
print("平方：", squares)

# 过滤：只要偶数
evens = [n for n in nums if n % 2 == 0]
print("偶数：", evens)

# 映射 + 过滤同时做
odd_squares = [n * n for n in nums if n % 2 == 1]
print("奇数的平方：", odd_squares)

# 字符串也可以推导（比如把一组词都转成大写，agent 处理文本常用）
words = ["hello", "world", "agent"]
upper_words = [w.upper() for w in words]
print("转大写：", upper_words)

# dict 推导式
num_to_double = {n: n * 2 for n in nums}
print("数字->两倍：", num_to_double)


# ============================================================
# 4. for 遍历元素（Python 直接遍历元素，不是下标）
# ============================================================
sep("4. for 遍历元素")

messages = ["你好", "在吗", "再见", "谢谢"]

# 直接遍历元素（不用 for i in range(len(...))）
for msg in messages:
    print(f"  收到消息：{msg}")

# 需要下标时用 enumerate（同时拿索引和元素）
for i, msg in enumerate(messages):
    print(f"  第 {i} 条：{msg}")

# 遍历 dict（前面演示过 items()，这里再强调下）
config = {"model": "claude", "temperature": 0.7}
for k, v in config.items():
    print(f"  配置项 {k} = {v}")

# range 生成数字序列
for i in range(3):          # 0, 1, 2
    print(f"  计数：{i}")


# ============================================================
# 5. 小练习（把 TODO 补全，跑一跑）
# ============================================================
sep("5. 小练习")

# 练习 A：用列表推导式，从下面列表里筛出长度大于 3 的字符串
words_list = ["hi", "hello", "ok", "agent", "go", "python"]
long_words = [w for w in words_list if len(w) > 3]   # TODO: 补全
print("长度>3 的词：", long_words)

# 练习 B：用 f-string 打印「当前温度是 23.5 度」这句话
temperature = 23.5
# TODO: 用 f-string 打印
print(f"当前温度是{temperature}度")

# 练习 C：给下面的字典新增一个键 "city"，值为 "上海"
user_info = {"name": "小明", "age": 20}
# TODO: 新增键
user_info["city"] = "上海"
print("新增city后:",user_info)

print("\n全部练习跑完了，看看输出是否符合预期。")
