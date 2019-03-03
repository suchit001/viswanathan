from django.contrib.auth.models import AbstractUser
from django.db import models
from dashboard.models import collaborations

class CustomUser(AbstractUser):

    TYPE_CHOICES = (
        (0,'DIRECTOR'),
        (1,'SECRETARIAT'),
        (2,'GUIDE'),
        (3,'STUDENT'),
    )
    name = models.CharField(max_length=250,default='suchit')
    type = models.IntegerField(choices=TYPE_CHOICES, default=3)
    contact = models.IntegerField(default=100)

    def _str_(self):
        return str(self.username)
#
# class Guide(models.Model):
#     guide_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     guide_subject = models.CharField(max_length=100,default='maths')
#
#     def __str__(self):
#         return str(self.guide_id)
#
#
# class Student(models.Model):
#     student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='customstudent')
#     guide = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='customguide')
#
#     def __str__(self):
#         return str(self.student_id)



class sec_details(models.Model):
    designation = models.CharField(max_length=100)
    sec_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.sec_id)

class Director_details(models.Model):
    designation = models.CharField(max_length=100)
    director_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.director_id)

class Std_details(models.Model):
    study_purpose = (
        ('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')
    )
    st_study_purpose = models.CharField(max_length=100, choices=study_purpose)
    st_collab_id = models.ForeignKey(collaborations, on_delete=models.CASCADE)
    st_designation = models.CharField(max_length=100, default=False)
    any_pub = models.TextField(default=False)
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
         return str(self.student_id)

class Principal_investigator(models.Model):
    P_Dept = models.CharField(max_length=100)
    p_designation = models.CharField(max_length=100)
    pricipal_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
         return str(self.pricipal_id)
