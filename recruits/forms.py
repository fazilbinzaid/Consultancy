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
                  'designation',
                  'current_ctc',
                  'expected_ctc',
                  'location',
                  'notice_period',
                  'resume',
                  'recording',
                  )


    def clean(self):
        current_ctc = self.cleaned_data.get('current_ctc')
        expected_ctc = self.cleaned_data.get('expected_ctc')
        notice_period = self.cleaned_data.get('notice_period')
        if int(current_ctc) < 0 or int(expected_ctc) < 0:
            raise forms.ValidationError("Enter a valid cost to company.")
        if int(expected_ctc) < current_ctc:
            raise forms.ValidationError("Expected CTC can't be less than Current one.")
        if int(notice_period) < 30:
            raise forms.ValidationError("Least notice period must be 30 days.")
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


    def clean(self):
        for form in self.forms:
            exp = form.cleaned_data.get('exp')
            if int(exp) < 0:
                raise forms.ValidationError("Enter a valid number for years of experience.")
            return super(CustomInlineFormset, self).clean()

class CustomSkillFormset(forms.BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        super(CustomSkillFormset, self).__init__(*args, **kwargs)
        if self.forms:
            for form in self.forms:
                for field in form.fields:
                    form.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        for form in self.forms:
            exp = form.cleaned_data.get('exp')
            if int(exp) < 0:
                raise ValidationError("Enter a valid number for years of experience.")
        return super(CustomSkillFormset, self).clean()



profile_formset = inlineformset_factory(Profile, Skillset,
                                    fields=('skill','exp',),
                                    # extra=2,
                                    # max_num=3,
                                    formset=CustomInlineFormset,
                                    can_delete=True,
                                    )
Skillformset = modelformset_factory(Skillset,
                                    fields=('skill', 'exp'),
                                    # can_delete=True,
                                    # extra=2,
                                    formset=CustomSkillFormset,
                                    )
