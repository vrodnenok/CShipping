# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse 
from django.views.decorators.csrf import *
from django.contrib.auth.decorators import login_required
from CShipping.models import Vessel, Voyage, Port, Vport
import datetime

@login_required(login_url='/accounts/login/')
@csrf_exempt 
def new_voyage (request):
    print request.GET.get('vsl_id')
    if request.GET.get('voy_id')=='null':
        return create_first_voyage(request.GET.get('vsl_id'))
    return render_to_response('new_voyage.html')

def create_first_voyage(vsl_id):
    vsl = Vessel.objects.get(id=vsl_id)
    voy_name = '001-%s' % (vsl.vsl_name)
    return render_to_response('new_voyage.html', {'voy':voy_name, 'vsl':vsl.vsl_name})