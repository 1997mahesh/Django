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
def homePage_1(request):
    return render (request, "index.html")


# Pass Data From Django View to Template
def homePage_2(request):
    data = {
        'title':'Home Page New',
        'bdata':'Welcome to Home Page'
    }
    return render (request, "index.html", data) 


# Using Django Template FOR Loop
def homePage_3(request):
    data = {
        'title':'Home Page New',
        'bdata':'Welcome to Home Page',
        'clist':['PHP', 'Java', 'Python', 'C', 'C++'],
        'student_details': [
            {'name':'Pradeep', 'phone':95648574},
            {'name':'mahesh', 'phone':634748574},
            {'name':'neha', 'phone':88648574},
        ]
    }
    return render (request, "index_For_Loop.html", data) 


