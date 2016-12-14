from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import (authenticate,
                                 )
from .models import (CustomUser, Profile,
                    #  Skillset,
                     )


class ProfileForm(forms.ModelForm):
    django_exp = forms.IntegerField(label='Experience in Django (years)')
    angular_exp = forms.IntegerField(label='Experience in Other (years)')
    class Meta:
        model = Profile
        fields = ('name',
                  'email',
                #   'skillset',
                  'django_exp',
                  'angular_exp',
                  'resume',
                  'interview',
                #   'user',
                  )

    def clean(self):
        name = self.cleaned_data.get('name')
        subject = "Alert to new profile Update"
        contact_message = "New profile with name %s have been created"%(name)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,]
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

        cleaned_data = super(ProfileForm, self).clean()
        return cleaned_data

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer is active")
        return super(UserLoginForm, self).clean()
