# version 0.001

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from CShipping.models import Voyage, Vessel

urlpatterns = patterns('voyages.views',                 
                    
    url(r'^$','new_voyage'),
)
