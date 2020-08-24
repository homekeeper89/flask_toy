import pytest

# Constants

DUCKDUCKGO_HOME = "https://duckduckgo.com/"


# Hooks 에러 발생시 잡아줌 단 직접
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"Step failed: {step}")

