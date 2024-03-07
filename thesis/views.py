from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm 

import datetime
today = datetime.date.today()

import joblib

loaded_stack_model = joblib.load("static/joblib/stack_lr.joblib")
# print(loaded_stack_model)
# TODO
# change color if fake or real
# FAKE = 9A01014A
# Real = 019A5A4A
# Default =  4E5DDD4A
# if else in here 
radialColor="#4E5DDD4A"

def factCheck(text):
    factChecked = text

    return factChecked

def versionTwo(request):
     # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # process the data in form.cleaned_data as required
            # if else
            # redirect to a new URL:
            result = factCheck(form.cleaned_data['content'])
            print(result)
            
            return render(request, 'views/start_version2.html' , {"form": form, 'radialColor': "#019A5A4A" ,"todisplay": 3 , 'percentage': 20 })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    template = loader.get_template('views/start_version2.html')
    return render(request, 'views/start_version2.html' , {"form": form, 'radialColor': radialColor, 'todisplay': 1, 'percentage': 75 })
    
  
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def startPage(request):
    template = loader.get_template('views/start_page.html')
    return HttpResponse(template.render())

def aboutPage(request):
    template = loader.get_template('views/about_page.html')
    return HttpResponse(template.render({'year': today.strftime('%G')}))
   
def faqPage(request):
    template = loader.get_template('views/faq_page.html')
    return HttpResponse(template.render({'year': today.strftime('%G')}))

