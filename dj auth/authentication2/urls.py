from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from authentication2.views import panda

urlpatterns = [
    path('',panda, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]