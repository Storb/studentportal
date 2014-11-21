from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy


class RegisterUser(FormView):
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy('register_success')
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterUser, self).form_invalid(form)


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

def register_success(request):
    return render(request, 'accounts/register_success.html')


