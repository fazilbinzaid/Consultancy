from django.contrib import admin
from .models import (Consultancy, Profile,
                     Skillset,
                     )

admin.site.register(Consultancy)
admin.site.register(Profile)
admin.site.register(Skillset)
