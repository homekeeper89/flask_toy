import pytest


@pytest.fixture(params=["ora", "pg", "sqlite"])
def params(request):
    return request.param


@pytest.mark.skip
def test_param(params):
    assert params == "ora"


try:
    import cx_Oracle as ora
except ImportError:
    ora = None

needs_ora = pytest.mark.skipif(ora is None, reason="No Oracle installed")


@pytest.fixture(
    params=["pg", needs_ora("ora"),]
)
def sample_db(request):
    return request.param


def test_sample(sample_db):
    print(sample_db)
    assert sample_db is "pg"

