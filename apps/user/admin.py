from django.contrib import admin
from .models import User
from django.contrib.auth.models import Permission


class CustomUserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
