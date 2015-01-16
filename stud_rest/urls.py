from django.conf.urls import patterns, include, url
from django.contrib import admin
from stud_db import urls as stud_db_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stud_rest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(stud_db_urls, namespace='stud_db_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
