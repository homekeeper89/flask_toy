import os
import datetime
from pathlib import Path

from small_app.utils.custom_logger import CustomLogger


def get_path(path_name: str) -> str:
    now = datetime.datetime.now().strftime("%Y_%m_%d")
    path = os.getcwd() + f"/small_app/{path_name}" + now
    return path


def test_logger_should_work():
    path = get_path("test")

    res = Path(path)
    import ipdb

    ipdb.set_trace()
    assert path is not None
