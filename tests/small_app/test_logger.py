import os
import datetime
from pathlib import Path

from small_app.utils.custom_logger import CustomLogger


def get_path(path_name: str) -> str:
    now = datetime.datetime.now().strftime("%Y_%m_%d")
    path = os.getcwd() + f"/small_app/{path_name}/" + now
    return path


def test_logger_should_work():
    path = get_path("test")

    file_path = Path(path)

    if file_path.exists():
        file_path.rmdir()

    custom_logger = CustomLogger("file")
    custom_logger.make_log("test")

    file_path = Path(path)

    assert file_path.exists()
