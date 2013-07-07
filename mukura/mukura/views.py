'''
Created on 06-Jul-2013

@author: srihari
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return render_to_response("index.html", RequestContext(request))

def about(request):
    return render_to_response("about.html", RequestContext(request))

def travel(request):
    return render_to_response("travel.html", RequestContext(request))

def contact(request):
    return render_to_response("contact.html", RequestContext(request))
