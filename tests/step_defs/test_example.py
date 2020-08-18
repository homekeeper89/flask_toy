from pytest_bdd import scenario, given, when, then, parsers


@scenario("../features/arguments.feature", "Arguments for given, when, thens")
def test_arguments():
    print("i am test")  # 제일 마지막에 실행
    pass


@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="start_cucumbers")
def start_cucumbers(start):
    print("start cucumber")  # 첫번째로 실행
    return dict(start=start, eat=0)


@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(start_cucumbers, eat):
    print("eat cucumber")  # 두번째로 실행
    start_cucumbers["eat"] += eat


@then(parsers.parse("I should have {left:d} cucumbers"))
def should_have_left_cucumbers(start_cucumbers, start, left):
    print("left cucumber")  # 세번째로 실행
    assert start_cucumbers["start"] == start
    assert start - start_cucumbers["eat"] == left

