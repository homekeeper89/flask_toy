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


@pytest.mark.xfail(reason="known parser issue")
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


# xfail을 사용하는 이유?
# The xfail test should pass and is expected to pass in the future, but is expected to fail given the current state of the software.
# flask_toy/tests/test_skip.py xX 의 결과, 즉 대문자 X는 통과했음을 의미한다.


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")),
    ],
    ids=["kk", "kk", "kk", "kk", "kk", "kk", "kk",],
)
def test_increment(n, expected):
    assert n + 1 == expected


# NOTE : hello_world를 사용할 수 있다.
def hello_world(*args, **kwargs):
    return f"Hello World{args}"


# pytest -x --pdb fail 뜨면 멈춤
# pytest test_skip.py --pdb --pdbcls=IPython.terminal.debugger:Pdb
# > ipdb를 사용하는 것
@pytest.mark.my_marker.with_args(hello_world)
def test_with_args():
    assert 3 == 2
