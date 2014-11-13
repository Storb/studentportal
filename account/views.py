from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm


def login(request):
    if request.method == "GET":
        username = request.GET.get('username','')
        password = request.GET.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

    return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('accounts/loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('accounts/logout.html')


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
    return render_to_response('accounts/register_user.html', context)


def register_success(request):
    return render_to_response('accounts/register_success.html')


# def login(request, template_name='account/login.html',
# authentication_form=AuthenticationForm,
#           extra_context=None):
#     if request.method == "POST":
#         form = authentication_form(data=request.POST)
#         if form.is_valid():
#             # Use default setting if redirect_to is empty
#             # if not redirect_to:
#             redirect_to = LOGIN_REDIRECT_URL
#
#             user = form.get_user()
#             auth_login(request, user)
#             user.profile.save()
#             if request.session.test_cookie_worked():
#                 request.session.delete_test_cookie()
#
#             return HttpResponseRedirect(redirect_to)
#     else:
#         form = authentication_form(request)
#     request.session.set_test_cookie()
#     context = {
#         'form': form,
#     }
#     if extra_context is not None:
#         context.update(extra_context)
#     return TemplateResponse(request, template_name, context)
#
#
#
# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")
#
# def register(request):
#     context = {}
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/")
#     else:
#         form = UserCreationForm()
#         context = {'form': form,}
#     return render(request, "accounts/register_user.html", context)
