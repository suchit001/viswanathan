from django.shortcuts import redirect, render
from users.models import Student,Guide,CustomUser

def panda(request):
    if(request.user.is_authenticated):


        if(request.user.type == 3):
            student = Student.objects.filter(student_id__in = CustomUser.objects.filter(username= str(request.user.username )))
            guidename = Guide.objects.filter(guide_id__in = CustomUser.objects.filter(username = student[0].guide))

            print(student[0].student_id)
            print(guidename)

            return redirect('student_dashboard')
        elif(request.user.type == 0):
            return redirect('director_dashboard')
        elif(request.user.type == 1):
            return redirect('secretariat_dashboard')
        elif(request.user.type == 2):
            return redirect('guide_dashboard')

        else:
            context = {
                'type' : 'coder',
            }
        return render(request, 'users/home.html', context=context)

    else:
        return redirect('login')
