from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'is_staff']
    list_filter = ('username',)
    search_fields = ('username', 'email', 'medical_code')

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.role = 'doctor'
    #     super().save_model(request, obj, form, change)
    #


admin.site.register(User, UserAdmin)