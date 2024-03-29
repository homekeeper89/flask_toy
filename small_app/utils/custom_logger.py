import os
import datetime
from pathlib import Path


class CustomLogger:
    def __init__(self, category: str):
        self.category = category
        self.date = datetime.datetime.now().strftime("%Y_%m_%d")

    def make_log(self, contents: dict):
        if self.category == "file":
            self.make_file_log(contents)
        elif self.category == "sms":
            self.make_sms_log(contents)
        else:
            self.make_cloud_log(contents)

    def make_file_log(self, contents: dict):
        file_path = os.getcwd() + "/small_app/log/" + self.date
        Path(file_path).mkdir(parents=True, exist_ok=True)

        state = contents.get("state", "delete")
        message = contents.get("message", "")

        today = f"{file_path}/[{state}]"
        with open(today, "a") as file:
            file.write(message + "\n")

    def make_sms_log(self):
        pass

    def make_cloud_log(self):
        pass
