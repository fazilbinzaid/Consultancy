from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return "profiles/"

# class Skillset(models.Model):
#     skill = models.CharField(max_length=10, primary_key=True)
#
#     def __str__(self):
#         return self.skill


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profiles')
    name = models.CharField(max_length=40)
    # skillset = models.ManyToManyField(Skillset, related_name='skills')
    email = models.EmailField()
    django_exp = models.IntegerField()
    angular_exp = models.IntegerField()
    resume = models.FileField(blank=True)
    interview = models.FileField(blank=True)

    def __str__(self):
        return self.name

    # @property
    # def name(self):
    #     return ' '.join([str(self.first_name), str(self.last_name)])

    def get_absolute_url(self):
        return "/profiles/%i/" % self.id
