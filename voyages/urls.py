# version 0.001

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from CShipping.models import Voyage, Vessel

urlpatterns = patterns('voyages.views',                 
                    
    url(r'^$','new_voyage'),
    url(r'^update/$','update'),
    url(r'^vsl_id/(?P<vsl_id>\w+)/voy_id/(?P<voy_id>\w+)$', 'new_voyage')
)
