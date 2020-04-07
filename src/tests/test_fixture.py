from . import *
import random


@pytest.fixture
def rnd():
    return random.random()


@pytest.fixture
def fixture_a(rnd):
    return rnd


@pytest.fixture
def fixture_b(rnd):
    return rnd


def test_rnd(rnd):
    print(rnd)


def test_multiple(fixture_a, fixture_b):
    assert fixture_a == fixture_b


@pytest.fixture(params=["ora", "pg", "sqlite"])
def params(request):
    return request.param


try:
    import cs_Oracle as ora
except ImportError:
    ora = None

needs_ora = pytest.mark.skipif(ora is None, reason="No Oracle installed")


@pytest.fixture(params=["pg", needs_ora("ora")])
def param_two(request):
    return request.param


def test_param(params):
    assert params == "ora"


def test_param_two(param_two):
    assert param_two is True

