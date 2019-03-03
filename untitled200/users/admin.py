from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomStudentCreationForm, CustomUserChangeForm
from .models import CustomUser,Guide,Student


class CustomUserAdmin(UserAdmin):
    add_form = CustomStudentCreationForm
    model = CustomUser
    list_display = ['username', 'name','contact']


admin.site.register(CustomUser, admin_class=CustomUserAdmin)
admin.site.register(Guide)
admin.site.register(Student)

admin.site.site_header="Cateina Admin"
admin.site.site_title="Cateina Admin"