"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project1 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUs),
    path('course/', views.course),
    path('home/', views.home),
    
    # Creating a Dynamic URL
    path('course/<courseName>', views.courseDetails),
    
    
    #Render an HTML Template as Response
    #path('', views.homePage_1),
    
    
    #Pass Data From Django View to Template
    #path('', views.homePage_2),
    
    
    # Using Django Template FOR Loop
    path('', views.homePage_3),
    
    
    


    
]
