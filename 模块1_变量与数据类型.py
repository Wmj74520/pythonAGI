# ============================================================
# 第 1 课：变量与数据类型
# 怎么用：在 VSCode 里打开这个文件，点右上角的 ▶ 运行
# 每段下面的 print 会把结果打印出来，对着看就行
# ============================================================


print("===== 1. 变量：给东西贴个标签 =====")

# 变量 = 一个贴了名字的盒子
name = "吴明俊"   # 拿个盒子，贴上 name 标签，把"小明"放进去
age = 23        # 再拿个盒子，贴上 age 标签，放 18

print(name)              # 打印 name 盒子里的东西 → 小明
print(age)               # → 18
print("我叫", name)       # 可以一次打印多个 → 我叫 小明


print("\n===== 2. 数字：加减乘除 =====")

a = 10
b = 3
print(a + b)   # 加 → 13
print(a - b)   # 减 → 7
print(a * b)   # 乘 → 30
print(a / b)   # 除 → 3.3333333333333335
print(a // b)  # 整除（只要整数部分）→ 3
print(a % b)   # 取余（余数）→ 1


print("\n===== 3. 字符串：一段文字 =====")

s = "你好，AI agent"
print(s)           # → 你好，AI agent
print(len(s))      # 有几个字 → 7
print(s[0])        # 第 1 个字 → 你
print(s[0:2])      # 前 2 个字 → 你好
print("一" + "二")  # 拼接 → 一二

# f-string：把变量塞进一句话里
print(f"我叫{name}，今年{age}岁")   # → 我叫吴明俊，今年23岁


print("\n===== 4. 列表：一张清单 =====")

fruits = ["苹果", "香蕉", "橘子"]
print(fruits)        # → ['苹果', '香蕉', '橘子']
print(fruits[0])     # 第 1 个 → 苹果

fruits.append("蓝莓")  
fruits.append("葡萄")  # 往末尾加一个
print(fruits)        # → ['苹果', '香蕉', '橘子', '葡萄']
fruits.remove("苹果")  
fruits.remove("香蕉")  # 删掉香蕉
print(fruits)        

print(len(fruits))
print(fruits)   


print("\n===== 5. 字典：通讯录 =====")

phone1 ={"吴明俊": "1369722732200","黄丽玲": "1877154587200"}
phone = {"小明": "13800138000", "小红": "13900139000"}
print(phone["小明"])                # 按名字查号码 → 13800138000
print(phone1["吴明俊"])

phone1["吴晓帅"]="1872716298800"
phone["小刚"] = "13700137000"    # 加一个新联系人
print(phone)
print(phone1)

# 把通讯录一条一条念出来
for name_key, number in phone1.items():
    print(name_key,"的电话是",number)
for name_key, number in phone.items():
    print(name_key, "的电话是", number)


print("\n===== 6. 集合：不重复的东西 =====")

tags = {"python", "学习", "python", "AI"}  # 重复的 python 会被去掉
print(tags)        # 注意：集合打印出来的顺序不固定，没关系
print(len(tags))   # 去重后有几个 → 3


# ============================================================
# 动手练习（改一改、运行、看变化）：
# 1) 把 age 改成你自己的年龄，再运行，看输出变没变
# 2) 往 fruits 里加上你爱吃的水果，再运行
# 3) 往 phone 里加上你朋友的名字和电话，再运行
# 4) 用 f-string 打印 "我叫小明，今年18岁" 这样的句子
# ============================================================
