#from django.conf.urls import patterns, include, url 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^voyages/', include('voyages.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
    url(r'^$', 'CShipping.views.index'), 
    url(r'^xhr_test$','CShipping.views.xhr_test'),                                    
    url(r'^blog/', include('blog.urls')),    
    url(r'^distances/', include('distances.urls')),
    ) + staticfiles_urlpatterns()
