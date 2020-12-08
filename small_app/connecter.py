from selenium import webdriver
import requests


class Connecter:
    WAITTING_SECONDS = 15

    def __init__(self, target_url):
        self.target_url = target_url

    def get(self):
        res = requests.get(self.target_url)
        return res

    def execute(self):
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.implicitly_wait(self.WAITTING_SECONDS)

        driver.get(self.target_url)

        return driver.quit()

