from http import HTTPStatus

from django.contrib.auth.models import User

from django.test import TestCase
from django.urls import reverse_lazy

from boxes.models import Box


class BoxesTests(TestCase):
    def test__create_user_for_box(self):
        box = Box.objects.create(name='test box', slug='test-box')
        url = reverse_lazy('create-box-user', kwargs={'slug': box.slug})
        expected_username = 'test-user'
        response = self.client.post(
            url, data={'username': expected_username, 'password1': 'yxcv1234', 'password2': 'yxcv1234'},
            follow=True
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        assert response.wsgi_request.user.is_authenticated
        assert 'Create a new message' in str(response.content)
        assert User.objects.filter(username=expected_username).exists()
