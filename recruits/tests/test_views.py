from django.test import TestCase, Client
from recruits.views import (login_view,
                            profile_list,
                            )
from django.contrib.auth import login, get_user_model


# class Setup_Class(TestCase):
#
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(email="user@user.com",
#                                               password="123",
#                                               name="test_user",
#                                               address="Palarivattom",
#                                               is_staff=True,
#                                               )
#
# class User_views_test(TestCase):
#
#     def test_login_view(self):
#         user_login = self.client.login(email="user@user.com", password="123")
#         self.assertTrue(user_login)
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 302)
