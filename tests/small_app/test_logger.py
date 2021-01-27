from small_app.utils import CustomLogger


def test_logger_should_workd():
    lg = CustomLogger()
    res = lg.record()
    assert res is True
