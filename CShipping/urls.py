#from django.conf.urls import patterns, include, url 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^$', 'CShipping.views.index'), 
    url(r'^xhr_test$','CShipping.views.xhr_test'),                                    
    url(r'^blog/', include('blog.urls')),    
    url(r'^distances/', include('distances.urls')),
    url(r'^examples/', include('examples.urls')),
    ) + staticfiles_urlpatterns()
