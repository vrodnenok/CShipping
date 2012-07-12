from django.conf.urls import patterns, include, url
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('examples.views',
        #Dajax URLS
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    
    #Website Examples
    url(r'^multiply/?$','multiply'),
    url(r'^maps/','maps'),
    url(r'random/?$','random_example'),
    url(r'forms/?$','form_example'),
    url(r'pagination/?$','pagination_example'),
    url(r'full_form/?$','full_form_example'),
    url(r'flickr/?$','flickr_example'),
    
    #Api examples
    #url(r'apiexamples/?$','dajaxexamples.apiexamples.views.api_examples'),
    url(r'^', 'index'),
)
