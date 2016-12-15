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

    def get_full_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return "profiles/"



class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profiles')
    name = models.CharField(max_length=40)
    # skillset = models.ManyToManyField(Skillset, related_name='profiles')
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=20)
    current_ctc = models.DecimalField(max_digits=3, decimal_places=2)
    expected_ctc = models.DecimalField(max_digits=3, decimal_places=2)
    notice_period = models.IntegerField()
    resume = models.FileField(upload_to='docs/', blank=True)
    recording = models.FileField(upload_to='media/', blank=True)
    recording_optional = models.FileField(blank=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return "/profiles/%i/" % self.id


class Skillset(models.Model):
    profile = models.ForeignKey(Profile, related_name='skills')
    skill = models.CharField(max_length=10, primary_key=True)
    exp = models.IntegerField()

    class Meta:
        unique_together = ('profile', 'skill')

    def __str__(self):
        return self.skill
