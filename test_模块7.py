# 第 7 课：pytest 测试文件
# 规矩：文件名必须以 test_ 开头，测试函数也以 test_ 开头，pytest 才认

from 模块7_被测函数 import add, is_adult, divide


def test_add():
    # 断言：我认为 add(2, 3) 算出来应该等于 5
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_is_adult_true():
    assert is_adult(18) == True


def test_is_adult_false():
    assert is_adult(17) == False


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(10, 0) is None

def test_add_negative():
    assert add(-1,-1) == -2
