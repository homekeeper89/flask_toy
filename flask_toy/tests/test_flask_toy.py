from flask_toy import __version__
import pytest
@pytest.mark.version
def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass

# pytest -k send_http
# pytest -v -k "not send_http"
# pytest -k "http or quick" -v