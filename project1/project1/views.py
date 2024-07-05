from django.http import HttpResponse

# How to render an HTML template as Response
from django.shortcuts import render



def aboutUs(request):
    return HttpResponse ("Hello Mahesh")

def home(request):
    return HttpResponse ("Home page")

def course(request):
    return HttpResponse ("this is course page")



# Creating a Dynamic URL

def courseDetails(request, courseName):
    return HttpResponse (courseName)



# How to render an HTML template as Response

def homePage(request):
    data={
        'title':'New Home Page'
    }
    return render(request,"home.html", data)


