# 第 7 课：这些是"要被测试"的普通函数
# 测试 = 写另一个程序，自动检查这些函数算得对不对


def add(a, b):
    return a + b


def is_adult(age):
    return age >= 18


def divide(a, b):
    if b == 0:
        return None
    return a / b
