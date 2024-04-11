from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        data = request.POST
        User.objects.create(username=data['username'],
                            password=make_password(data['password'])).save()

        return redirect('/auth/login')

    return render(request, 'register.html')


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            next_page = request.GET.get('next', '/')

            return redirect(next_page)

        context['message'] = 'Invalid username or password !'

        return render(request, 'login.html', context)

    return render(request, 'login.html')


@login_required(login_url='/auth/login')
def logout_view(request):
    logout(request)
    return redirect('/')
