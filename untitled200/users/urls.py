# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('signup/guide', views.SignUpGuide.as_view(), name='signup_guide'),
    path('signup/student', views.SignUpStudent.as_view(), name='signup_student'),
]