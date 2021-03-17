from django.test import TestCase

from ..models import Message
from .factories import MessageFactory


class TestMessageManager(TestCase):
    def test__messages__archived_queryset(self):
        MessageFactory.create_batch(5, archived=True)
        messages = Message.objects.all()

        assert messages.archived().count() == 5

    def test__messages__not_archived_queryset(self):
        MessageFactory.create_batch(5, archived=False)
        messages = Message.objects.all()

        assert messages.not_archived().count() == 5

    def test__messages__archived_manager(self):
        MessageFactory.create_batch(5, archived=True)

        assert Message.objects.archived().count() == 5

    def test__messages__not_archived_manager(self):
        MessageFactory.create_batch(5, archived=False)

        assert Message.objects.not_archived().count() == 5
