from django.conf.urls import patterns, url
from account import views


urlpatterns = patterns('',
    # user auth urls
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register_user/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
)