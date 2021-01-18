# selenium 객체를 00 패턴을 통해서 재구성


class CustomElement:
    # 엘리먼트가 현재 화면에 있는지 확인하는 메서드는 필수로 세팅

    def __init__(self, elem):
        self.elem = elem

    def is_elem_in_screen(self) -> bool:
        pass
