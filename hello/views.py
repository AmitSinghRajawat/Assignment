from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests

#shipy is the file contains git API information
import shipy

	

# Create your views here.
def index(request):
    # replace gitUrl for value to other git urls 
    gitUrl = "https://github.com/Shippable/support/issues"

   # separates url into tokens
    parts= (gitUrl).split("/")

    # joins url to get JSON api 
    apiLink=parts[0]+"//api."+parts[2]+"/repos/"+("/".join(parts[3:]))

    #calling shipy source code, show table contains required information
    showTable=shipy.getDays(apiLink)
    return HttpResponse('<pre>' + "open Issues : "+str(showTable["open_Issues"])+ '</pre>''<pre>' + "open issues that were opened more than 7 days ago : "+str(showTable["More_than_7_days"])+ '</pre>''<pre>' + "open issues that were opened more than 24 hours ago but less than 7 days ago : "+str(showTable["Within_1_week"])+ '</pre>''<pre>' + "open issues that were opened in the last 24 hours : "+str(showTable["Within_24_hours"])+ '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

