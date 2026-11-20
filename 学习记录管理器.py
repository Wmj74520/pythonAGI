# ============================================================
# 阶段一项目：个人学习记录管理器
# ============================================================

import json
from datetime import datetime
DATA_FILE = "records.json"   # 所有记录都存在这个文件里


def load_records(filename):
    """从文件读出所有记录；如果文件还不存在，就返回一个空清单"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_records(records, filename):
    """把所有记录写进文件"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def add_record(records, date, content):
    """往清单里加一条记录：日期 + 内容"""
    records.append({"date": date, "content": content})
    return records


def list_records(records):
    """把记录整理成一行行文字，返回一个列表（方便显示，也方便以后测试）"""
    lines = []
    for i, r in enumerate(records):
        lines.append(f"{i + 1}. [{r['date']}] {r['content']}")
    return lines


def is_valid_date(text):
    """判断输入的日期是否符合 YYYY-MM-DD 格式"""
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ============================================================
# 增删查改功能
# ============================================================  
def delete_record(records, index):
    """删除指定索引的记录"""
    if index < 1 or index > len(records):
        raise ValueError("没有第%d条记录。"%index)
    records.pop(index -1)
    return records

def update_record(records, index, date, content):
    """修改第 index 条"""
    if index < 1 or index > len(records):
        raise ValueError("没有第 %d 条记录" % index)
    records[index - 1] = {"date": date, "content": content}
    return records


def find_records(records, keyword):
    """按关键词搜索，返回内容列表"""
    results = []
    for i, r in enumerate(records):
        if keyword in r["date"] or keyword in r["content"]:
            results.append((i + 1, r))
    return results
# ============================================================
# 增删查改功能
# ============================================================  


def main():
    """主程序：显示菜单，等用户输入"""
    records = load_records(DATA_FILE)
    print("=== 个人学习记录管理器 ===")

    while True:
        print("\n1) 添加记录   2) 查看记录   3) 删除   4) 修改   5) 搜索   6)退出"  )
        choice = input("请选择：").strip()

        if choice == "1":
            # 日期不合法
            while True:
                date = input("日期（格式 YYYY-MM-DD，如 2026-11-20）：").strip()
                if is_valid_date(date):
                    break
                print("日期不对！必须像 2026-11-20 这样，而且是真实日期。")

            # 内容不能为空
            while True:
                content = input("内容：").strip()
                if content:
                    break
                print("内容不能空！")
            add_record(records, date, content)
            save_records(records, DATA_FILE)
            print("添加成功！")

        elif choice == "2":
            lines = list_records(records)
            if not lines:
                print("还没有任何记录。")
            else:
                for line in lines:
                    print(line)
        elif choice == "3":
            if not records:
                print("还没有任何记录，无法删除。")
                continue
            for line in list_records(records):
                print(line)
            raw = input("要删除第几条？请输入数字:").strip()
            try:
                idx=int(raw)
            except ValueError:
                print("请输入有效的数字。")
                continue
            try:
                delete_record(records, idx)
                save_records(records, DATA_FILE)
                print("删除成功！")
            except ValueError as e:
                print("删除失败！",e)
        elif choice == "4":
            if not records:
                print("还没有记录，没法修改。")
                continue
            for line in list_records(records):
                print(line)
            raw = input("要修改第几条？输入序号：").strip()
            try:
                idx = int(raw)
            except ValueError:
                print("请输入数字序号。")
                continue
            while True:
                date = input("新日期(格式 YYYY-MM-DD):").strip()
                if is_valid_date(date):
                    break
                print("日期不对！请重输。")
            while True:
                content = input("新内容：").strip()
                if content:
                    break
                print("内容不能空！")
            try:
                update_record(records, idx, date, content)
                save_records(records, DATA_FILE)
                print("修改成功！")
            except ValueError as e:
                print("修改失败：", e)
        elif choice == "5":
            keyword = input("输入要搜索的关键词：").strip()
            if not keyword:
                print("关键词不能空。")
                continue
            results = find_records(records, keyword)
            if not results:
                print("没找到包含「%s」的记录。" % keyword)
            else:
                print("找到 %d 条：" % len(results))
                for idx, r in results:
                    print("%d. [%s] %s" % (idx, r["date"], r["content"]))
        elif choice == "6":

            print("再见！")
            break

        else:
            print("没有这个选项，请输入 1、2、3、4、5、6")


if __name__ == "__main__":
    main()
