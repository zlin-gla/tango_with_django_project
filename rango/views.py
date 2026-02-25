from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    about_page_url = '<a href="/rango/about/">About</a>'
    return HttpResponse("Rango says hey there partner! " + about_page_url)

def about(request):
    home_page_url = '<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page. " + home_page_url)

