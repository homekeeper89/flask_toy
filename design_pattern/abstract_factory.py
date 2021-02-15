import random


class PetShop:
    def __init__(self, animal_factory):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print(f"We have a lonely {pet}")
        print(f"It says {pet.speak()}")


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


def random_animal():
    return random.choice([Dog, Cat])()


# Show pets with various factories
def main():
    """
    # A Shop that sells only cats
    >>> cat_shop = PetShop(Cat)
    >>> cat_shop.show_pet()
    We have a lovely Cat
    It says meow
    # A shop that sells random animals
    >>> shop = PetShop(random_animal)
    >>> for i in range(3):
    ...    shop.show_pet()
    ...    print("=" * 20)
    We have a lovely Cat
    It says meow
    ====================
    We have a lovely Dog
    It says woof
    ====================
    We have a lovely Dog
    It says woof
    ====================
    """


if __name__ == "__main__":
    random.seed(1234)  # for deterministic doctest outputs
    import doctest

    doctest.testmod()
