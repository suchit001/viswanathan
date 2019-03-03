from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import BudgetForm
from .models import *
# Register your models here.


admin.site.register(Budget)
admin.site.register(Investigation2)
admin.site.register(Investigation1)
admin.site.register(Salaryy)
admin.site.register(Consumable)
admin.site.register(Capital_equip)
