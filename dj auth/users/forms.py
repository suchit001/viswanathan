from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Guide, Student


class CustomStudentCreationForm(UserCreationForm):

    guide = forms.ModelChoiceField(
        queryset= Guide.objects.all()
    )


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('name', 'username', 'email', 'type', 'contact','guide')

    def save(self):
        user = super().save(commit= False)
        user.type = 3
        user.save()
        guide = self.cleaned_data.get('guide')
        guide_parent = CustomUser.objects.filter(username = guide)

        guide_obj = Guide.objects.filter(guide_id=guide_parent)

        student = Student.objects.create(student_id=user)
        student.guide_id = guide_obj
        student.save()
        return user


class CustomGuideCreationForm(UserCreationForm):

    guide_subject = forms.CharField(label='Subject')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('name', 'username', 'email', 'type', 'contact','guide_subject')

    def save(self):
        user = super().save(commit = False)
        user.type = 2
        user.save()
        guide = Guide.objects.create(guide_id=user)
        guide.guide_subject = self.cleaned_data.get('guide_subject')
        guide.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'email')