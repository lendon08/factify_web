from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm 

import numpy as np
import datetime
today = datetime.date.today()
import re
import joblib


best_estimator = joblib.load("static/models/best_estimator.joblib")
stack_xgboost = joblib.load("static/models/stack_xgboost.joblib")
vectorizer = joblib.load('static/models/vectorizer.joblib')


# print(loaded_stack_model)
# TODO
# change color if fake or real
# FAKE = 9A01014A
# Real = 019A5A4A
# Default =  4E5DDD4A
# if else in here 


def factCheck(text):
    return stack_xgboost.predict_proba(text)

def vectorizer(text):
    return stack_xgboost.named_steps['vectorizer'].transform(text)

def versionTwo(request):
     # if this is a POST request we need to process the form data
    
    toDisplay = 1
    radialColor="#4E5DDD4A"
    percentage = 1.1
    estimators = list() 
    
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # process the data in form.cleaned_data as required
            # if else
            # redirect to a new URL:
            text = form.cleaned_data['content'].split(' ',0)
            result = factCheck(text)
          
            percentages = [(num * 100) for sublist in result for num in sublist]
            num = [round(num, 2) for num in percentages]
            vectorized  = vectorizer(text)

            # put in a list of all base estimator then remove "(any)"
            for x in stack_xgboost.named_steps['stacking'].estimators_:
                prob = x.predict_proba(vectorized)
                sub_predict = "Real"
                sub_percent = 1.1
                for y in prob:
                    if y[0] > y[1]:
                        sub_percent = format( y[0], ".2%")
                    else:
                        sub_predict = "Fake"
                        sub_percent = format( y[1], ".2%")
                    
                estimators.append([re.sub(r'\([^)]*\)', '', str(x)), sub_predict, sub_percent]) 
            
            # print(estimators)
         
            if num[0] > num[1] :
                toDisplay = 4
                radialColor = "#9A01014A"
                percentage = num[0]
            else:
                toDisplay = 3
                radialColor = '#019A5A4A'
                percentage = num[1]

            return render(request, 'views/start_version2.html' , {"form": form, 'radialColor': radialColor ,"todisplay": toDisplay , 'percentage': percentage, 
                                                                  'estimators': estimators })

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

