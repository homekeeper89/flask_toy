import requests


class Connecter:
    def __init__(self, target_url):
        self.target_url = target_url

    def get(self):
        res = requests.get(self.target_url)
        return res
