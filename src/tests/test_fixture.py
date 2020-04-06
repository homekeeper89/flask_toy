from . import *
import random


@pytest.fixture
def rnd():
    return random.random()


def test_rnd(rnd):
    print(rnd)
