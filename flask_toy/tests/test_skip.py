# 버젼에 따라서 테스트를 스킵하는 경우에 사용하면 될듯
import sys
import pytest

var_num = 30
# true이면 skip임
@pytest.mark.skipif(var_num > (10), reason="requires python3.6 or higher")
def test_skip_if_condition_is_true():
    assert var_num < 10

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100
# xfail을 사용하는 이유?
#The xfail test should pass and is expected to pass in the future, but is expected to fail given the current state of the software.