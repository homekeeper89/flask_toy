import factory
from datetime import datetime
from faker import Factory as FakerFactory
from src.model.models import User, Todos

faker = FakerFactory.create()


class UserFactory(factory.Factory):
    """ Define user factory
    """

    class Meta:
        model = User

    email = factory.Faker("safe_email")
    name = factory.LazyAttribute(lambda x: faker.name())

    todos = factory.RelatedFactoryList(".tests.factories.TodosFactory", size=3)


class TodosFactory(factory.Factory):
    """Define todo factory
    """

    class Meta:
        model = Todos

    title = factory.LazyAttribute(lambda x: faker.name())
    created_at = factory.LazyAttribute(lambda x: datetime.now())
    updated_at = factory.LazyAttribute(lambda x: datetime.now())

    user = factory.SubFactory(UserFactory, samples=[])


# https://simpleit.rocks/python/django/setting-up-a-factory-for-one-to-many-relationships-in-factoryboy/
class TodoWithUserFactory(UserFactory):
    @factory.post_generation
    def players(obj, create, extracted, **kwargs):
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
                myapp.factories.PlayerFactory(team=obj)
        else:
            import random

            number_of_units = random.randint(1, 10)
            for n in range(number_of_units):
                myapp.factories.PlayerFactory(team=obj)
