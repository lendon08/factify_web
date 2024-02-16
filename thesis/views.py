from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def startPage(request):
    template = loader.get_template('start_page.html')
    return HttpResponse(template.render())

def aboutPage(request):
    template = loader.get_template('about_page.html')
    return HttpResponse(template.render())
   
def updatePage(request):
    template = loader.get_template('update_page.html')
    return HttpResponse(template.render())

