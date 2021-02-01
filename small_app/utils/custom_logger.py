class CustomLogger:
    def __init__(self, category: str):
        self.category = category

    def make_log(self, path: str, contents: str):
        if self.category == "file":
            return True
