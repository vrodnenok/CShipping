# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse 
from django.views.decorators.csrf import *
from django.contrib.auth.decorators import login_required
from CShipping.models import Vessel, Voyage, Port, Vport
from time import strftime

@login_required(login_url='/accounts/login/')
@csrf_exempt 
def update(request):
    req = request.POST
    if req.get('action') == 'add_port':
        
    #                port: $trow.eq(0).children().children().val(),
        vp = Vport()
        vp.voyages_id = req.get('voyages_id')
        vp.port = req.get('port')
        vp.agent = req.get('agent')
        print req.get('port')
        print vp.port
        vp.cargo = req.get('cargo')
        vp.ldrate = req.get('ldrate')
        vp.est_da = req.get('est_da')
        vp.ops_type = req.get('ops_type')
        vp.turn = req.get('turn')
        vp.save()
        testport = Vport.objects.filter(id = vp.id)
        print testport.port
        return HttpResponse('%s port added' %(testport.port))
    #                turn: $trow.eq(1).children().children().val(),
    #                ops_type: $trow.eq(2).children().children().val(),
    #                agent: $trow.eq(3).children().children().val(),
    #                cargo: $trow.eq(4).children().children().val(),
    #                ldrate: $trow.eq(5).children().children().val(),
    #                est_da: $trow.eq(6).children().children().val(),

    print req
    return HttpResponse(u'OK')

@login_required(login_url='/accounts/login/')
@csrf_exempt 
def new_voyage (request, vsl_id, voy_id):
    print vsl_id + ' --- '
    print voy_id
    if voy_id=='null':
        print 'first voyage processing'
        cyear = strftime('%Y')
        vsl = Vessel.objects.get(id=vsl_id)
        voy = Voyage()
        voy.voy_number = '001-%s-%s' % (vsl.vsl_name, cyear)
        print voy.voy_number
        voy.vessels_id = vsl.id
        voy.save()
        ports = Port.objects.filter()
        allports = []
        allports.append('At sea')
        for port in ports:
            if port.fport not in allports:
                allports.append(port.fport)
            if port.tport not in allports:
                allports.append(port.tport)
            allports = sorted(allports)
        return render_to_response('new_voyage.html', {'voyages_id':voy.id, 'voy':voy.voy_number, 'vsl':vsl.vsl_name, 'ports':allports, 'vsl_id':vsl.id})
    else:
        print ('do something new')
        print 'new voyage processing'
        cyear = strftime('%Y')
        vsl = Vessel.objects.get(id=vsl_id)
        print vsl.vsl_name
        pvoy = Voyage.objects.get(id=voy_id)
        newvoynumber = pvoy.voy_number.split('-') # = '001-%s-%s' % (vsl.vsl_name, cyear)
        nwn = int(newvoynumber[0])
        nwn += 1
        print nwn
        voy=Voyage()
        voy.voy_number = '00%s-%s-%s' % (nwn, vsl.vsl_name, cyear)
        voy.vessels_id = vsl.id
        voy.save()
        ports = Port.objects.filter()
        allports = []
        allports.append('At sea')
        for port in ports:
            if port.fport not in allports:
                allports.append(port.fport)
            if port.tport not in allports:
                allports.append(port.tport)
            allports = sorted(allports)
        return render_to_response('new_voyage.html', {'voyages_id':voy.id, 'voy':voy.voy_number, 'vsl':vsl.vsl_name, 'ports':allports, 'vsl_id':vsl.id})
    return render_to_response('new_voyage.html')

