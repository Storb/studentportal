from django.conf.urls import patterns, url
from account import views


urlpatterns = patterns('',
    # user auth urls
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register_user/$', views.RegisterUser.as_view(), name='register_user'),
    url(r'^register_success/$', views.SuccessRegView.as_view(), name='register_success'),
    url(r'^accounts/user_detail/(?P<pk>\d+)$', views.UserDetail.as_view(), name='user_detail'),
)