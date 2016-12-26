from django import forms
from questions.models import Question, Language, Framework


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('id',
                  'framework',
                  'question_text',
                  )

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('id',
                  'tag')

class FrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ('id',
                  'language',
                  'name')
