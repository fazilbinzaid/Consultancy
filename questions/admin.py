from django.contrib import admin
from .models import Question, Language, Framework

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


class FrameworkAdmin(admin.ModelAdmin):
    model = Framework
    inlines = [QuestionInline]


class FrameworkInline(admin.TabularInline):
    model = Framework
    extra = 3


class LanguageAdmin(admin.ModelAdmin):
    model = Language
    inlines = [FrameworkInline]


admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Question)
