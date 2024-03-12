from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm 

import numpy as np
import datetime
today = datetime.date.today()

import joblib


best_estimator = joblib.load("static/models/best_estimator.joblib")
stack_xgboost = joblib.load("static/models/stack_xgboost.joblib")


base_knn = joblib.load('static/models/base/baseline_knn.joblib')
base_lr = joblib.load('static/models/base/baseline_lr.joblib')
base_nb = joblib.load('static/models/base/baseline_nb.joblib')
base_rf = joblib.load('static/models/base/baseline_rf.joblib')
base_svm = joblib.load('static/models/base/baseline_svm.joblib')

# print(loaded_stack_model)
# TODO
# change color if fake or real
# FAKE = 9A01014A
# Real = 019A5A4A
# Default =  4E5DDD4A
# if else in here 


def factCheck(text):
    return stack_xgboost.predict(text.split(' ',0))



def versionTwo(request):
     # if this is a POST request we need to process the form data
    
    toDisplay = 1
    radialColor="#4E5DDD4A"
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # process the data in form.cleaned_data as required
            # if else
            # redirect to a new URL:
            result = factCheck(form.cleaned_data['content'])
            real = np.count_nonzero(result == 1)
            fake = np.count_nonzero(result == 0)
            print("real: " +' '+ str(real))
            print("fake: " +' '+ str(fake))
            if fake > real :
                toDisplay = 4
                radialColor = "#9A01014A"
            else:
                toDisplay = 3
                radialColor = '#019A5A4A'

            return render(request, 'views/start_version2.html' , {"form": form, 'radialColor': radialColor ,"todisplay": toDisplay , 'percentage': 100 })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'views/start_version2.html' , {"form": form, 'radialColor': radialColor, 'todisplay': toDisplay, 'percentage': 75 })
    

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

