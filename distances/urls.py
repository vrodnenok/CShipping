# version 0.001
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from distances.models import Ports

urlpatterns = patterns('distances.views',                 
    url(r'^update$', 'updates'),
    url(r'^$', 'distances'),
)+ staticfiles_urlpatterns()