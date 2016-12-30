from django.contrib import admin
from .models import (CustomUser, Profile,
                     Skillset,
                     )

class SkillsetInline(admin.StackedInline):
    model = Skillset
    extra = 3

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [SkillsetInline]


admin.site.register(CustomUser)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skillset)
