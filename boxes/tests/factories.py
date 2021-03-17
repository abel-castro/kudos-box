import factory
from django.contrib.auth.models import User

from ..models import Box, Message


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    is_staff = True
    password = "yxcv1234"
    username = "test-user"


class BoxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Box

    name = factory.Sequence(lambda n: "Box %d" % n)
    slug = factory.Sequence(lambda n: "slug-%d" % n)


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    title = factory.Sequence(lambda n: "title_%d" % n)
    text = factory.Faker("text")
    box = factory.SubFactory(BoxFactory)
