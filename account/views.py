from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import FormView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, View, TemplateView


class RegisterUser(FormView):
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy('register_success')
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)


class UserDetail(DetailView):
    model = User
    template_name = "accounts/user_detail.html"


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url = "/"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(TemplateResponseMixin, View):

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth.logout(self.request)
        return HttpResponseRedirect('/')


class SuccessRegView(TemplateView):
    template_name = "accounts/register_success.html"



