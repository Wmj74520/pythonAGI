# ============================================================
# 第 3 课：出错别慌 + 把内容存进文件 + JSON
# 用法：VSCode 打开，点右上角 ▶ 运行
# 运行后，这个文件夹里会多出 demo.txt 和 person.json，可以打开看看
# ============================================================


print("===== 1. 什么是「报错」，怎么接住它（try/except）=====")

# 除以 0 会出错。把「可能出错的代码」放进 try，出错就走 except
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("接住了：不能除以 0")

# 打开一个不存在的文件，也会出错
try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("接住了：这个文件不存在")


print("\n===== 2. 写文件：把内容存进电脑 =====")

# "w" = 写（会清空原文件再写）
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("你好，这是我写进文件的第一行\n")
    f.write("第二行\n")
print("已写入 demo.txt")

# 读：把文件内容读出来
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("读出来的内容是：")
print(content)


print("\n===== 3. 追加：往文件末尾再加东西 =====")

# "a" = 追加（在末尾加，不清空原内容）
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("第三行（我是后来加的）\n")

with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())


print("\n===== 4. 按行读文件（配合 for 循环）=====")

with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("这一行是：", line.strip())   # strip() 去掉行尾的换行


print("\n===== 5. JSON：规整地存数据 =====")

import json

# 一个字典（就是第 1 课学的「通讯录」）
person = {"name": "小明", "age": 18, "city": "北京"}

# 把字典变成 JSON 存进文件
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)
print("已存进 person.json（可以用记事本打开看看）")

# 从文件读回来，变回字典
with open("person.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("读回来是：", data)
print("名字是：", data["name"])


# ============================================================
# 动手练习：
# 1) 把 try 里的 10 / 0 改成 10 / 2，再运行，看还报不报错
# 2) 往 demo.txt 再追加一行 "第四行"，再运行
# 3) 把 person 换成你自己的信息（姓名、年龄、城市），重新存、再读
# 4) 用记事本打开 person.json 看一看，长什么样
# ============================================================
