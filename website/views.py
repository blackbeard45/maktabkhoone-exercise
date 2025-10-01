from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("<h1>This is the index page view.</h1>")

def about_view(request):
    return HttpResponse("<h1>This is the about page view.</h1>")

def contact_view(request):
    return HttpResponse("<h1>This is the contact page view.</h1>")
