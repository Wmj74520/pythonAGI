# 第 3 步：给「学习记录管理器」写 pytest 测试
# 运行方法：在 vcdoework 里，激活 .venv 后敲 pytest
import pytest

from 学习记录管理器 import (
    add_record,
    list_records,
    is_valid_date,
    delete_record,
    update_record,
    find_records,
)


# ---------- 1. 日期校验 ----------
def test_is_valid_date_ok():
    assert is_valid_date("2026-11-20") == True


def test_is_valid_date_bad():
    assert is_valid_date("2026-11-20,今天") == False
    assert is_valid_date("abc") == False
    assert is_valid_date("2026-13-45") == False


# ---------- 2. 添加记录 ----------
def test_add_record():
    records = []
    add_record(records, "2026-11-20", "学了Python")
    assert len(records) == 1
    assert records[0] == {"date": "2026-11-20", "content": "学了Python"}


# ---------- 3. 列出记录 ----------
def test_list_records():
    records = [
        {"date": "2026-11-20", "content": "第一条"},
        {"date": "2026-11-21", "content": "第二条"},
    ]
    lines = list_records(records)
    assert lines == ["1. [2026-11-20] 第一条", "2. [2026-11-21] 第二条"]


# ---------- 4. 删除记录 ----------
def test_delete_record_normal():
    records = [
        {"date": "a", "content": "1"},
        {"date": "b", "content": "2"},
    ]
    delete_record(records, 1)
    assert len(records) == 1
    assert records[0]["date"] == "b"


def test_delete_record_out_of_range():
    records = [{"date": "a", "content": "1"}]
    with pytest.raises(ValueError):
        delete_record(records, 5)


# ---------- 5. 修改记录 ----------
def test_update_record_normal():
    records = [{"date": "a", "content": "旧"}]
    update_record(records, 1, "2026-11-22", "新")
    assert records[0] == {"date": "2026-11-22", "content": "新"}


def test_update_record_out_of_range():
    records = [{"date": "a", "content": "1"}]
    with pytest.raises(ValueError):
        update_record(records, 0, "2026-11-22", "新")


# ---------- 6. 搜索记录 ----------
def test_find_records():
    records = [
        {"date": "2026-11-20", "content": "学了Python"},
        {"date": "2026-11-21", "content": "学了Git"},
    ]
    results = find_records(records, "Python")
    assert len(results) == 1
    assert results[0][0] == 1
    assert results[0][1]["content"] == "学了Python"
