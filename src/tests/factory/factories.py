import factory
from datetime import datetime
from faker import Factory as FakerFactory
from src.model.models import User, Todos
from pytest_factoryboy import register

faker = FakerFactory.create()


class UserFactory(factory.Factory):
    """ Define user factory
    """

    class Meta:
        model = User

    email = factory.Faker("safe_email")
    name = factory.LazyAttribute(lambda x: faker.name())


class TodosFactory(factory.Factory):
    """Define todo factory
    """

    class Meta:
        model = Todos

    title = factory.LazyAttribute(lambda x: faker.name())
    created_at = factory.LazyAttribute(lambda x: datetime.now())
    updated_at = factory.LazyAttribute(lambda x: datetime.now())

    user = factory.SubFactory(UserFactory)
