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
