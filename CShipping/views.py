from django.shortcuts import render_to_response
from django.views.decorators.csrf import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse
#from django.utils import simplejson
from models import Vessel, Voyage, Operation, Port




@login_required(login_url='/accounts/login/')
@ensure_csrf_cookie
@csrf_protect
def index(request):
    vessels=Vessel.objects.filter()
#    return HttpResponse(vessels)
    return render_to_response('index.html', 
                              {'vessels':vessels}, context_instance=RequestContext(request))
    
@login_required(login_url='/accounts/login/')
@csrf_exempt
def xhr_test(request):
    message = ""
    if request.is_ajax():
        print request.POST
        if request.POST.get('vsl_id'):
            vsl_id=request.POST['vsl_id']
            voyages=Voyage.objects.filter(vessels_id=vsl_id)
            for voy in voyages:
                message += '<option value="%s">%s</option>' % (voy.id, voy.voy_number)
        elif request.POST.get('voy_id'):
            print "processing request"
            ports = Port.objects.filter()
            allports = []
            allports.append('At sea')
            for port in ports:
                if port.fport not in allports:
                    allports.append(port.fport)
                if port.tport not in allports:
                    allports.append(port.tport)
            allports = sorted(allports)
            voy_id=request.POST['voy_id']
            ops=Operation.objects.filter(voyages_id=voy_id)
            print 'voyage selected'
            message += "<table border='2' id=voyages_table> <th> C/P date</th>"
            message += "<th> Vessels location</th><th> Coordinates </th><th>Type of operation</th>"
            message += "<th> Action </th>"
            for op in ops:
                message += "<tr id = '%s'>" % (op.ops_id) 
                message += "<td><input value='%s'> </input></td>" % (op.date.strftime("%d/%m/%y %H:%M")) 
                message += "<td><select>"
                message += "<option>%s</option>" % (op.location)
                for port in allports:
                    if port != op.location:
                        message +="<option>%s</option>" % (port)
                message += "</select>"
                message += "<td><input value='%s'> </input></td>" % (op.coords)
                message += "<td><input value='%s'> </input></td>" % (op.ops_type)
                message += "<td><button class='tab_btn'>Full form edit</button></td></tr>"
            message += "</table>"
            print message
    else:
        message = "Sorry, your browser doesnt support AJAX"
    return HttpResponse(message)