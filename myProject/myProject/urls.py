from django.contrib import admin
from django.urls import path, include
from myApp.urls import *
urlpatterns = [
    # url admin
    path('admin/', admin.site.urls), 
    # url home 
    path('', include('myApp.urls')),      
]
