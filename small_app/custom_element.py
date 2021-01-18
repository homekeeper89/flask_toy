# selenium 객체를 00 패턴을 통해서 재구성


class CustomElement:
    # 엘리먼트가 현재 화면에 있는지 확인하는 메서드는 필수로 세팅

    def __init__(self, driver, elem):
        self.elem = elem
        self.driver = driver

    def is_elem_in_screen(self) -> bool:
        # https://stackoverflow.com/questions/34771094/how-can-i-check-if-an-element-is-completely-visible-on-the-screen
        elem_left_bound = self.elem.location.get("x")
        elem_top_bound = self.elem.location.get("y")
        elem_width = self.elem.size.get("width")
        elem_height = self.elem.size.get("height")
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem_height

        win_upper_bound = self.driver.execute_script("return window.pageYOffset")
        win_left_bound = self.driver.execute_script("return window.pageXOffset")
        win_width = self.driver.execute_script("return document.documentElement.clientWidth")
        win_height = self.driver.execute_script("return document.documentElement.clientHeight")
        win_right_bound = win_left_bound + win_width
        win_lower_bound = win_upper_bound + win_height

        return all(
            (
                win_left_bound <= elem_left_bound,
                win_right_bound >= elem_right_bound,
                win_upper_bound <= elem_top_bound,
                win_lower_bound >= elem_lower_bound,
            )
        )
