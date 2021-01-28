import os
import datetime

from small_app.utils.custom_logger import CustomLogger


def get_path() -> str:
    now = datetime.datetime.now().strftime("%Y_%m_%d")
    path = os.getcwd() + "/small_app/log/" + now
    return path


def test_logger_should_work():
    path = get_path()
    print(path)
    assert path is not None
