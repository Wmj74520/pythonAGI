# ============================================================
# 第 2 课：让电脑做选择、重复干活、打包小工具
# 怎么用：VSCode 打开这个文件，点右上角 ▶ 运行
# 注意：if / for / while / def 下面的代码要缩进（前面空 4 格）
# ============================================================


print("===== 1. 条件判断：如果……就……否则…… =====")

score = 75

# 如果分数 >= 60，就打印"及格"，否则打印"没及格"
if score >= 60:
    print("及格了")      # 前面空 4 格，表示这句属于 if 管
else:
    print("没及格")

# 多种情况：if / elif / else
score2 = 85
if score2 >= 90:
    print("优秀")
elif score2 >= 60:       # 否则如果
    print("及格")
else:                    # 以上都不满足
    print("不及格")


print("\n===== 2. for 循环：让电脑重复做 =====")

# 把清单里的东西一个一个拿出来
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print("我喜欢吃", fruit)

# 重复 5 次
for i in range(5):
    print("第", i + 1, "次")

# 把 1 加到 10
total = 0
for n in range(1, 11):
    total = total + n
print("1 加到 10 等于", total)


print("\n===== 3. while 循环：只要条件成立就一直做 =====")

count = 0
while count < 3:
    print("现在是第", count + 1, "轮")
    count = count + 1      # 别忘了让 count 变大，否则会永远循环
print("循环结束")


print("\n===== 4. 函数：把常用的事打包成一个小工具 =====")

# 定义一个小工具，名字叫 greet，需要一个"名字"才能用
def greet(name):
    print("你好，", name)

# 用这个小工具
greet("小明")
greet("小红")

# 带返回值的函数：给它两个数，它把和"还"给你
def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)


print("\n===== 5. 模块：别人写好的工具包，拿来就用 =====")

import random    # 随机数工具包

S = random.randint(1,10)
while True:
 scanf = int(input("请输入一个 1 到 10 的整数："))
 if scanf == S: 
    print("恭喜你，猜对了！")
    break
 elif scanf < S:
     print(f"你猜的数小了{scanf}-10")
 else:
     print(f"你猜的数大了1-{scanf}")
import math      # 数学工具包
print("16 的平方根:", math.sqrt(16))

import datetime  # 日期时间工具包
print("现在时间:", datetime.datetime.now())


# ============================================================
# 动手练习：
# 1) 把 score 改成 50，再运行，看 if 输出变没变
# 2) 用 for 循环打印 1 到 5 每个数的平方（就是自己乘自己）
#    提示：for n in range(1, 6):  print(n * n)
# 3) 自己写一个函数 say_hi(name)，打印 "hi, 名字"，再调用它
# 4) （挑战）用 while 写一个"猜数字"小游戏：
#    - 电脑心里想一个数（用 random.randint(1, 10)）
#    - 让你输入猜的数（input()）
#    - 大了/小了给提示，猜对就结束
#    （这个不会也没关系，下一课我们会一起写）
# ============================================================
