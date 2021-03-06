# Create your views here.

from django.shortcuts import render_to_response 
from django.template.loader import render_to_string
from django.views.decorators.csrf import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from models import Vessels, Voyages, Operations, Ports

@login_required(login_url='/accounts/login/')
@ensure_csrf_cookie
@csrf_protect
def distances(request):
    print request
    ports=Ports.objects.filter()
#    return HttpResponse(vessels)
    if request.is_ajax():
        if request.POST.get('action')=='update':
            print 'update'
            return
    return render_to_response('distances.html', 
                              {'ports':ports }, context_instance=RequestContext(request))
    
@login_required(login_url='/accounts/login/')
@csrf_exempt    
def updates(request):
    print request.POST
    if request.is_ajax():
        if request.POST.get('action')=='update':
            dist=Ports()
            dist.id=request.POST.get('id')
            dist.fport=request.POST.get('fport')
            dist.tport=request.POST.get('tport')
            dist.distance=request.POST.get('distance')
            dist.save()
            print dist.id
            return HttpResponse('ok')
        elif request.POST.get('action')=='add':
            ports=Ports.objects.filter()
            fport=request.POST.get('fport').lower()
            tport=request.POST.get('tport').lower()
            for port in ports:
                if port.fport.lower() == fport:
                    if port.tport.lower() == tport:
                        return HttpResponse('exists')
            for port in ports:
                if port.tport.lower() == fport:
                    if port.fport.lower() == tport:
                        return HttpResponse('exists')
            dist=Ports()
            #dist.id=request.POST.get('id')
            dist.fport=request.POST.get('fport')
            dist.tport=request.POST.get('tport')
            dist.distance=request.POST.get('distance')
            dist.save()
            print dist.id
            return HttpResponse('ok')
        elif request.POST.get('action')=='find':
            resp = "<table id='distances_table' border = 1 cellpadding=2 cellspacing=1 >"
            fltr = request.POST.get('filter')
            fports = Ports.objects.filter(fport__istartswith = fltr)
            tports = Ports.objects.filter(tport__istartswith = fltr)
            allports = fports | tports
            for port in allports:
                resp+="<tr value='%s'>" % (port.id)
                resp+="<td><input value='%s'/></td>" % (port.fport)
                resp+="<td><input value='%s'/></td>" % (port.tport)
                resp+="<td><input value='%s'/></td>" % (port.distance)
                resp+="<td><button class='update'>Update</button></td><td><button class='delete'>Delete</button></td></tr>"
            resp+="</table>"
            if len(allports) > 0:
                return HttpResponse(resp)
            else: 
                response = HttpResponse('Nothing has been found')
                return response
                
            # {% for port in ports %}
            # <tr value='{{port.id}}'>
            #     <td><input value='{{port.fport}}'/></td>
            #     <td><input value='{{port.tport}}'/></td>
            #     <td><input value='{{port.distance}}'/></td>
            #     <td><button class='update'>Update</button></td>
            # </tr>    
            # {% endfor %}
            #</table>
        elif request.POST.get('action')=='delete':
            try:
                Ports.objects.filter(id=request.POST.get('id')).delete()
                return HttpResponse ('deleted ok')
            except:
                return HttpResponse('server was unable to selete file')

    return HttpResponse('ajax no supported')