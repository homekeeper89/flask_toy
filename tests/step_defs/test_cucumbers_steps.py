from functools import partial
from tests.step_defs.test_serving import CONVERTERS
from pytest_bdd import scenario, given, when, then, parsers, scenarios

from src.bdd.cucumber import CucumberBasket


CONVERTERS = {"initial": int, "some": int, "total": int}

scenarios("../features/cucumbers.feature", example_converters=CONVERTERS)

EXTRA_TYPES = {"Number": int}
parse_num = partial(parsers.parse, extra_types=EXTRA_TYPES)
# @scenario("../features/cucumbers.feature", "Add cucumbers to a basket")
# def test_add():
#     pass


# @scenario("../features/cucumbers.feature", "Remove cucumbers from a basket")
# def test_remove():
#     pass


@given(parse_num("the basket has {initial:Number} cucumbers"))
@given("the basket has <initial> cucumbers")  # examples시 필요
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.parse("{some:Number} cucumbers are added to the basket", extra_types=EXTRA_TYPES))
@when("<some> cucumbers are added to the basket")
def add_cucumbers(basket, some):
    print(some)
    basket.add(some)


@when(parsers.parse("{some:d} cucumbers are removed from the basket"))
@when("<some> cucumbers are removed from the basket")
def remove(basket, some):
    basket.remove(some)


@then(parsers.parse("the basket contains {total:Number} cucumbers", extra_types=dict(Number=int)))
@then("the basket contains <total> cucumbers")
def basket_has_total(basket, total):
    assert basket.count == total
