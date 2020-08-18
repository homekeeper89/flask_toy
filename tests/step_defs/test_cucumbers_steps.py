from pytest_bdd import scenario, given, when, then, parsers

from src.bdd.cucumber import CucumberBasket


@scenario("../features/cucumbers.feature", "Add cucumbers to a basket")
def test_add():
    pass


@scenario("../features/cucumbers.feature", "Remove cucumbers from a basket")
def test_remove():
    pass


@given(parsers.parse("the basket has {initial:Number} cucumbers", extra_types=dict(Number=int)))
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(
    parsers.parse("{some:Number} cucumbers are added to the basket", extra_types=dict(Number=int))
)
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.parse("{some:d} cucumbers are removed from the basket"))
def remove(basket, some):
    basket.remove(some)


@then(parsers.parse("the basket contains {total:Number} cucumbers", extra_types=dict(Number=int)))
def basket_has_total(basket, total):
    assert basket.count == total
