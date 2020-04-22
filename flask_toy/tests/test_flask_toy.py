from flask_toy import __version__

@pytest.mark.version
def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize('test', 
[
    ('hello')
])
def test_id(test):
    assert test is not None
