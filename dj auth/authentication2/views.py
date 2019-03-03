from django.shortcuts import render, redirect

def panda(request):
    if(request.user.is_authenticated):
        if(request.user.type == 3):
            context = {
                'type' : 'student',
            }
        elif(request.user.type == 0):
            context = {
                'type' : 'director',
            }
        else:
            context = {
                'type' : 'coder',
            }
        return render(request, 'registration/home.html', context=context)

    else:
        return redirect('login')