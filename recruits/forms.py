from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import (authenticate,
                                 )
from .models import (CustomUser, Profile,
                     Skillset,
                     )
from django.forms import BaseInlineFormSet
from django.forms.models import inlineformset_factory, modelformset_factory


class SkillsetForm(forms.ModelForm):
    required_css_classes = 'form-control'

    class Meta:
        model = Skillset
        fields = ('skill',
                  'exp',
                  )

class ProfileForm(forms.ModelForm):

    current_ctc = forms.DecimalField(label='Current CTC (per annum)')
    expected_ctc = forms.DecimalField(label='Expected CTC (per annum)')
    notice_period = forms.IntegerField(label='Notice Period (months)')
    class Meta:
        model = Profile
        fields = ('name',
                  'email',
                #   'skills',
                  'current_ctc',
                  'expected_ctc',
                  'location',
                  'notice_period',
                  'resume',
                  'recording',
                  )

    def clean(self):
        # name = self.cleaned_data.get('name')
        # subject = "Alert to new profile Update"
        # contact_message = "New profile with name %s have been created"%(name)
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [from_email,]
        # send_mail(subject,
        #           contact_message,
        #           from_email,
        #           to_email,
        #           fail_silently=True)

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
                raise forms.ValidationError("This user does not exist right now.")
            if user.is_superuser:
                if not user.check_password(password):
                    raise forms.ValidationError("Incorrect Password")
            elif not user.password==password:
                raise forms.ValidationError("Incorrect the Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer is active")
        return super(UserLoginForm, self).clean()



class CustomInlineFormset(BaseInlineFormSet, forms.ModelForm):
    skill = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(CustomInlineFormset, self).__init__(*args, **kwargs)
        if self.forms:
            for form in self.forms:
                for field in form.fields:
                    form.fields[field].widget.attrs.update({'class': 'form-control'})


    # def clean(self):
    #     for form in self.forms:
    #         data = form.cleaned_data
    #         super(CustomInlineFormset, self).clean()


profile_formset = inlineformset_factory(Profile, Skillset,
                                    fields=('skill','exp',),
                                    # extra=1,
                                    # max_num=3,
                                    formset=CustomInlineFormset,
                                    can_delete=True,
                                    )
Skillformset = modelformset_factory(Skillset,
                                    fields=('skill', 'exp'),
                                    can_delete=True,
                                    # extra=3,
                                    )