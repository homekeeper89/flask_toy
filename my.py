def greeting(name: str) -> str:
    return "HELLO" + name


def p() -> None:
    print("heel")


greeting(3)
greeting(b"Alice")

from typing import List


def greet_all(names: List[str]) -> None:
    for name in names:
        print("hell" + name)


names = ["Alice", "Bob", "Charile"]
ages = [10, 20, 30]

kk = input("sdfas")
greet_all(kk)
