from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import UserCreateForm
from django.contrib.auth.models import User

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    form = {'form': user}
    return render(request,'accounts/user_detail.html', form)



def login(request):

    if request.method == "GET":
        username = request.GET.get('username','')
        password = request.GET.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/invalid')

    return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render(request,'accounts/invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    context = {}
    context.update(csrf(request))
    context['form'] = UserCreateForm()
    print(context)
    return render(request, 'accounts/register_user.html', context)


def register_success(request):
    return render(request, 'accounts/register_success.html')


