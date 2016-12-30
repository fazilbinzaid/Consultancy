from django.test import TestCase, Client
from recruits.forms import (UserLoginForm,
                            ProfileForm,
                            )
from django.contrib.auth import login, get_user_model
from recruits.models import (CustomUser,
                             )



class TestLoginForm(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email="user@user.com",
                                              password="123",
                                              )

    def test_login_form_valid(self):
        d = get_user_model().objects.all()
        print(d)
        form = UserLoginForm(data={'email': 'user@user.com', 'password': '123'})
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form = UserLoginForm(data={'email': 'user@user.com', 'password': ''})
        self.assertFalse(form.is_valid())
