from django.conf.urls import patterns, url
from . import views
# from students.views import GroupUpdate


urlpatterns = patterns('',
    url(r'^$', views.base, name='base'),
    url(r'^group_detail/(?P<group_id>\d+)/$', views.group_detail, name='group_detail'),
    url(r'^group_create/$',views.group_create, name='group_create'),
    url(r'^group_list/$', views.group_list, name='group_list'),
    url(r'^group_update/(?P<pk>\d+)$', views.group_update ,name='group_update'),
    url(r'^group_confirm_delete/$', views.group_confirm_delete, name='group_confirm_delete'),
    url(r'^group_delete/(?P<pk>\d+)$', views.group_delete ,name='group_delete'),
    url(r'^elder_list/$', views.elder_list, name='elder_list'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^student_create/$', views.student_create ,name = 'student_create'),
    url(r'^student_update/(?P<pk>\d+)$', views.student_update ,name = 'student_update'),
    url(r'^student_delete/(?P<pk>\d+)$', views.student_delete ,name='student_delete'),
    url(r'^student_confirm_delete/(?P<pk>\d+)$', views.student_confirm_delete, name='student_confirm_delete'),
    url(r'^settings/$', views.settings_show, name='settings_show'),
    # url(r'^group/$', GroupList.as_view() ,name='group'),
    # url(r'^group_delete/(?P<pk>\d+)$', views.GroupDelete.as_view() ,name='group_delete'),
    # url(r'^group_update/(?P<pk>\d+)$', GroupUpdate.as_view() ,name='group_update'),
)

