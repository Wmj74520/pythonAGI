# ============================================================
# 第 4 课：类和对象（做个模板，批量造东西）
# 用法：VSCode 打开，点右上角 ▶ 运行
# 这课有点抽象，跟着注释一句一句看，别急
# ============================================================


print("===== 1. 定义一个「模板」：学生 =====")

class Student:
    # 造学生的时候，会自动执行 __init__（初始化）
    def __init__(self, name, age):
        self.name = name    # self.name 就是"这个学生自己的名字"
        self.age = age      # self.age  就是"这个学生自己的年龄"

    # 定义学生的一个「动作」：自我介绍
    def introduce(self):
        print("我叫", self.name, "，今年", self.age, "岁")


print("===== 2. 照着模板，造两个具体的「学生」 =====")

s1 = Student("小明", 18)   # 造第一个学生
s2 = Student("小红", 17)   # 造第二个学生

s1.introduce()             # 我叫 小明 ，今年 18 岁
s2.introduce()             # 我叫 小红 ，今年 17 岁

print("s1 的名字是：", s1.name)
print("s2 的年龄是：", s2.age)


print("\n===== 3. 再用同样的办法，做一个「学习记录」模板 =====")

class LearningRecord:
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def show(self):
        print(f"[{self.date}] {self.content}")


r1 = LearningRecord("2026-11-17", "学了类和对象")
r2 = LearningRecord("2026-11-17", "写了 demo.py")

r1.show()
r2.show()


print("\n===== 4. 把一堆对象放进清单，再挨个处理 =====")

records = [r1, r2]
for r in records:
    r.show()


# ============================================================
# 动手练习：
# 1) 再照 Student 造一个学生，名字用你自己的，年龄随便
# 2) 把 LearningRecord 改成「Task」，字段换成 title 和 done
# 3) 造 3 条 Task 放进清单，用 for 循环全部打印出来
# ============================================================
