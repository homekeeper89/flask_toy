import factory
from datetime import datetime
from faker import Factory as FakerFactory
from src.model.models import User, Todos

faker = FakerFactory.create()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    """ Define user factory
    """

    class Meta:
        model = User

    email = factory.Faker("safe_email")
    name = factory.LazyAttribute(lambda x: faker.name())


class TodosFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Define todo factory
    """

    class Meta:
        model = Todos

    title = factory.LazyAttribute(lambda x: faker.name())
    created_at = factory.LazyAttribute(lambda x: datetime.now())
    updated_at = factory.LazyAttribute(lambda x: datetime.now())

    user = factory.SubFactory(UserFactory)


# https://simpleit.rocks/python/django/setting-up-a-factory-for-one-to-many-relationships-in-factoryboy/
class UserWithTodoFactory(UserFactory):
    @factory.post_generation
    def todos(obj, create, extracted, **kwargs):
        """
        If called like: TeamFactory(players=4) it generates a Team with 4
        players.  If called without `players` argument, it generates a
        random amount of players for this team
        """
        if not create:
            # Build, not create related
            return

        if extracted:
            for n in range(extracted):
                TodosFactory(user=obj)
        else:
            import random

            number_of_units = random.randint(1, 10)
            for n in range(number_of_units):
                TodosFactory(user=obj)
