import warnings
import pytest
def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1

def test_one():
    assert api_v1() == 1

# pytest -q test_show_warnings.py -W error::UserWarning , 에러 나옴

@pytest.mark.filterwarnings("ignore:api v1")
def test_two():
    assert api_v1() == 1