from customuser.models import user_type


def render(request, param):
    pass


def redirect(param):
    pass


def buyer(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return render(request, 'index.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return redirect('come')
    else:
        return redirect('login')


def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return render(request, 'index.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('index')
    else:
        return redirect('login')
