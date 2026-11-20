# -*- coding: utf-8 -*-
"""
Python 基础练习（第 2 课：函数进阶）
重点：默认参数、关键字参数、*args/**kwargs、lambda、函数作参数、可变默认参数坑

运行方式：python practice_functions.py
"""


def sep(title: str) -> None:
    """打印一个带标题的分隔线"""
    print("\n" + "=" * 50)
    print(f"### {title}")
    print("=" * 50)


# ============================================================
# 1. 默认参数
# ============================================================
sep("1. 默认参数")


def get_weather(city: str, days: int = 3, unit: str = "celsius") -> str:
    """查天气：days 和 unit 有默认值"""
    return f"查询 {city} 未来 {days} 天天气，单位 {unit}"


print(get_weather("北京"))                        # 全用默认
print(get_weather("北京", 7))                     # 改 days
print(get_weather("北京", unit="fahrenheit"))     # 只改 unit（用关键字参数）

# 注意：有默认值的参数必须放后面
# def bad(a=1, b):   # 这样会报语法错误
#     pass


# ============================================================
# 2. 关键字参数（调用时按名字传，顺序可打乱）
# ============================================================
sep("2. 关键字参数")

print(get_weather(city="上海", unit="fahrenheit", days=5))


# ============================================================
# 3. *args 和 **kwargs（agent 框架核心）
# ============================================================
sep("3. *args 和 **kwargs")


# *args：接收任意多个位置参数，打包成元组
def log_all(*args):
    print("收到位置参数（元组）：", args)
    for a in args:
        print("  -", a)


log_all("开始", 123, {"k": "v"})


# **kwargs：接收任意多个关键字参数，打包成字典
# 这就是 agent 框架把 LLM 返回的 JSON 参数传给工具函数的机制
def call_tool(tool_name: str, **kwargs):
    print(f"调用工具：{tool_name}")
    for key, value in kwargs.items():
        print(f"  参数 {key} = {value}")


call_tool("search", query="北京天气", limit=5)
call_tool("calculator", expression="3 + 5 * 2")


# 两者可以同时用（顺序：普通参数, *args, **kwargs）
def demo(a, *args, **kwargs):
    print(f"a={a}, args={args}, kwargs={kwargs}")


demo(1, 2, 3, name="x", age=20)


# ============================================================
# 4. lambda（一行匿名函数）
# ============================================================
sep("4. lambda")

double = lambda x: x * 2
print("double(5) =", double(5))

# 最常用场景：给 sorted 指定排序规则
tools = [
    {"name": "search", "priority": 3},
    {"name": "calculator", "priority": 1},
    {"name": "weather", "priority": 2},
]
sorted_tools = sorted(tools, key=lambda t: t["priority"])
print("按优先级排序：", sorted_tools)


# ============================================================
# 5. 函数是一等公民（函数可以当参数传）
# ============================================================
sep("5. 函数作参数 / 回调")


def apply_to_all(func, items):
    """对列表每个元素应用 func"""
    return [func(x) for x in items]


result = apply_to_all(lambda x: x * 2, [1, 2, 3])
print("每个元素乘 2：", result)

result2 = apply_to_all(str.upper, ["hello", "world"])
print("转大写：", result2)


# ============================================================
# 6. 经典坑：可变默认参数
# ============================================================
sep("6. 可变默认参数的坑")


# ❌ 错误写法：默认参数 [] 只在定义时创建一次，多次调用共享同一个列表
def add_item_bad(item, items=[]):
    items.append(item)
    return items


print("错误写法第一次调用：", add_item_bad(1))   # [1]
print("错误写法第二次调用：", add_item_bad(2))   # [1, 2]  ← 出问题了


# ✅ 正确写法：默认值用 None，函数内部再新建
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print("正确写法第一次调用：", add_item(1))   # [1]
print("正确写法第二次调用：", add_item(2))   # [2]  ← 正常了


# ============================================================
# 7. 小练习（补全 TODO）
# ============================================================
sep("7. 小练习")


# 练习 A：写一个 greet 函数，接收 name 和 greeting="你好"，返回问候语
def greet(name, greeting="你好"):
    # TODO: 返回 f"{greeting}，{name}！"
    pass


# 练习 B：写一个 summarize 函数，用 **kwargs 接收任意参数，打印"共 X 个参数"
def summarize(**kwargs):
    # TODO: 打印参数个数 len(kwargs)
    pass


# 练习 C：用 lambda + sorted，把下面列表按 price 从低到高排序
products = [
    {"name": "键盘", "price": 199},
    {"name": "鼠标", "price": 99},
    {"name": "显示器", "price": 1299},
]
# cheap_first = sorted(products, key=lambda ...)  # TODO: 补全并打印

print("\n练习 B、C 留给你补全后运行。")
