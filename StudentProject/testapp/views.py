from django.shortcuts import render
import datetime

# Create your views here.
date = datetime.datetime.now()
h = date.strftime("%Y")
def display(request):
    return render(request,'testapp/home.html',{'h':h})

def about(request):
    return render(request,'testapp/about.html')

def contact(request):
    return render(request,'testapp/contact.html')

def tech(request):
    return render(request,'testapp/tech.html')

def android(request):
    return render(request,'testapp/android.html')
