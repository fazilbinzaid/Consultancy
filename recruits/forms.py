from django import forms
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
            user = self.cleaned_data.get['consultancy']
            user = request.user
            cleaned_data = super(ProfileForm, self).clean({'consultancy': 'user'})
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
