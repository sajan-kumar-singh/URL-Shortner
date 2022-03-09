from django.shortcuts import render,HttpResponse
from pyshorteners import *
# Create your views here.
def home(request):
    return render(request,"add.html")
def add(request):
    fin=request.GET["evaluation_string"]
    url=Shortener()
    short_url=url.tinyurl.short(fin)
    return render(request,"result.html",{'x':short_url})
    
