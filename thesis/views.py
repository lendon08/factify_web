from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
import datetime
today = datetime.date.today()
print(today)


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def startPage(request):
    template = loader.get_template('views/start_page.html')
    return HttpResponse(template.render())

def versionTwo(request):
    template = loader.get_template('views/start_version2.html')
    return HttpResponse(template.render())

def aboutPage(request):
    
    template = loader.get_template('views/about_page.html')
    return HttpResponse(template.render({'year': today.strftime('%G')}))
   
def faqPage(request):
    template = loader.get_template('views/faq_page.html')
    return HttpResponse(template.render({'year': today.strftime('%G')}))
