from django.contrib import admin
from .models import UserProfile, Lead


admin.site.register(UserProfile)
admin.site.register(Lead)
