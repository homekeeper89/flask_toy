import selenium

from base.base_worker import BaseWorker


class SumgoWorker(BaseWorker):
    SELECTED_COUNT, DELETED_COUNT = 0, 0

    def __init__(self, conf: str = "conf.ini", is_delete: bool = True):
        super().__init__(conf)
        self.is_delete = is_delete

    def get_elem_by_xpath(self, xpath: str) -> selenium.webdriver.remote.webelement.WebElement:
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(f"[Error] {e}")
            return None

    def click(self, xpath: str):
        elem = self.get_elem_by_xpath(xpath)
        elem.click()

    def go_to_login_page(self):
        self.driver.get(self.user_data.target_url)
        login_xpath = '//*[@id="app-header"]/div[3]/ul/li[4]/a'
        self.click(login_xpath)

    def type_login_information(self):
        email_xpath = '//*[@id="__BVID__231"]'
        email_input = self.get_elem_by_xpath(email_xpath)
        email_input.send_keys(self.user_data.email)

        pwd_xpath = '//*[@id="__BVID__233"]'
        pwd_input = self.get_elem_by_xpath(pwd_xpath)
        pwd_input.send_keys(self.user_data.password)

        login_submit_elem = self.get_elem_by_xpath(
            '//*[@id="app-body"]/div/div/form/div/div[4]/button'
        )
        login_submit_elem.click()

    def execute(self):
        pass


if __name__ == "__main__":
    sw = SumgoWorker("conf.ini")
    sw.go_to_login_page()
    sw.type_login_information()
