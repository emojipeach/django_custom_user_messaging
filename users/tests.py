# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.test import TestCase

User = get_user_model()


class CustomUserModelTests(TestCase):
    """ Tests the CustomUser model. """

    def setUp(self):
        User.objects.create_user(
            username='testicle',
            first_name='bob',
            last_name='bobberts',
            email='test@ic.le',
            )

    def test_username(self):
        user = User.objects.get(username='testicle')
        self.assertEqual(user.username, 'testicle')
    
    def test_first_name(self):
        user = User.objects.get(username='testicle')
        self.assertEqual(user.first_name, 'bob')
    
    def test_last_name(self):
        user = User.objects.get(username='testicle')
        self.assertEqual(user.last_name, 'bobberts')

    def test_email(self):
        user = User.objects.get(username='testicle')
        self.assertEqual(user.email, 'test@ic.le')

class TestCalls(TestCase):
    
    def setUp(self):
        User.objects.create_user(
            username='testicle',
            first_name='bob',
            last_name='bobberts',
            email='test@ic.le',
            password='test',
            )

    def test_call_login_view_loads(self):
        self.client.login(username='testicle', password='test')
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_call_login_view_fails_blank(self):
        self.client.login(username='user', password='test')
        response = self.client.post(reverse_lazy('login'), {}) # blank data dictionary
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')
        