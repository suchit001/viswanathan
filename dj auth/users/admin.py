from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomStudentCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomStudentCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email','type']

admin.site.register(CustomUser, CustomUserAdmin)