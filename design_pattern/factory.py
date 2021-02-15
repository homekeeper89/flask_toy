from abc import ABCMeta, abstractclassmethod


class BaseExtractor(metaclass=ABCMeta):
    @abstractclassmethod
    def parse_data(self, data):
        pass


class JsonExtractor(BaseExtractor):
    def __init__(self, data):
        self.data = data

    def parse_data(self, data):
        print("json")


class XmlExtractor(BaseExtractor):
    def __init__(self, data):
        self.data = data

    def parse_data(self, data):
        print("xml")


def extractor_factory(data):
    if data == "json":
        extractor = JsonExtractor
    else:
        extractor = XmlExtractor
    return extractor(data)


if __name__ == "__main__":
    extrator = extractor_factory("json")
    extrator.parse_data("json")

    extrator = extractor_factory("xml")
    extrator.parse_data("xml")

