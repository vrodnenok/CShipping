# Create your views here.
from django.shortcuts import render_to_response

def new_voyage (request):
    return render_to_response('new_voyage.html')
