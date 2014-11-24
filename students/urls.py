from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns('',
    url(r'^$', views.base, name='base'),
    url(r'^settings/$', views.settings_show, name='settings_show'),
    url(r'^custom_tag/$', views.custom_tags, name='custom_tags'),
    url(r'^group_create/$', views.GroupCreate.as_view() ,name='group_create'),
    url(r'^group_detail/(?P<pk>\d+)$', views.GroupDetail.as_view() ,name='group_detail'),
    url(r'^groups_list/$', views.GroupList.as_view() ,name='groups_list'),
    url(r'^group_delete/(?P<pk>\d+)$', views.GroupDelete.as_view() ,name='group_delete'),
    url(r'^group_update/(?P<pk>\d+)$', views.GroupUpdate.as_view() ,name='group_update'),
    url(r'^students_list/$', views.StudentList.as_view() ,name='students_list'),
    url(r'^student_update/(?P<pk>\d+)$', views.StudentUpdate.as_view() ,name='student_update'),
    url(r'^student_detail/(?P<pk>\d+)$', views.StudentDetail.as_view() ,name='student_detail'),
    url(r'^student_delete/(?P<pk>\d+)$', views.StudentDelete.as_view() ,name='student_delete'),
    url(r'^student_create/$', views.StudentCreate.as_view(), name='student_create'),
)

