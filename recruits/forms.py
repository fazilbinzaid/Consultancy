from django import forms
from .models import (Consultancy, Profile,
                     Skillset,
                     )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',
                  'gender',
                  'email',
                  'skillset',
                  'consultancy',
                  )
