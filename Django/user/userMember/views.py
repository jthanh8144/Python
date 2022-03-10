from django.http import HttpResponse
from django.shortcuts import redirect, render
from . forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'userMember/register.html', {'rF': rF})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('register success')


class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'userMember/login.html', {'lF': lF})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user:private')
        else:
            return HttpResponse('login fail')


class privateUser(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'userMember/private.html')

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('user:login')
