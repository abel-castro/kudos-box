from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from guardian.shortcuts import assign_perm

from boxes.models import Message

from .factories import BoxFactory, MessageFactory, UserFactory


class BoxesTests(TestCase):
    def test__create_user_for_box(self):
        box = BoxFactory.create()
        url = reverse_lazy("create_box_user", kwargs={"slug": box.slug})
        expected_username = "test-user"
        response = self.client.post(
            url,
            data={
                "username": expected_username,
                "password1": "yxcv1234",
                "password2": "yxcv1234",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        assert response.wsgi_request.user.is_authenticated
        assert "Create a new message" in str(response.content)
        assert User.objects.filter(username=expected_username).exists()

    def test__archive_messages(self):
        user = UserFactory.create()
        box = BoxFactory.create()
        assign_perm("view_box", user, box)
        MessageFactory.create_batch(5, box=box)

        assert Message.objects.not_archived().count() == 5
        assert Message.objects.archived().count() == 0

        url = reverse_lazy("archive_box_messages", kwargs={"slug": box.slug})
        response = self.client.get(url)

        assert response.status_code == HTTPStatus.FOUND

        assert Message.objects.not_archived().count() == 0
        assert Message.objects.archived().count() == 5
