from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    TYPE_CHOICES = (
        (0,'DIRECTOR'),
        (1,'SECRETARIAT'),
        (2,'GUIDE'),
        (3,'STUDENT'),
    )
    name = models.CharField(max_length=250)
    type = models.IntegerField(choices=TYPE_CHOICES)
    contact = models.IntegerField()

    def _str_(self):
        return str(self.username)


class Guide(models.Model):
    guide_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    guide_subject = models.CharField(max_length=100)

    def __str__(self):
        return str(self.guide_id)


class Student(models.Model):
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide,on_delete=models.SET_NULL,null=True)


# class Director(models.Model):
#     director_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
#     designation = models.CharField(max_length= 100)