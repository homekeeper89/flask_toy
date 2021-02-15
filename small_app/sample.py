from abc import ABCMeta, abstractmethod


class Human(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = "part" + name
        self.age = "part" + age


class Asian(Human):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


if __name__ == "__main__":
    kk = Asian("aa", "aa", "aa")
    mm = Asian("mm", "mm", "mm")
    print(kk.__dict__)
    print()
    print(mm.__dict__)
