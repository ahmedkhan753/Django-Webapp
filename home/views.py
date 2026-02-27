from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Render the home index page"""
    context={
        "variable":"hello this is a test variable",
        "variable2":"this is another test variable"
    }
    return render(request, "index.html", context)

def about(request):
    """Display the about page"""
    return HttpResponse("this is about page")

def services(request):
    """Display the services page"""
    return HttpResponse("this is services page")

def contact(request):
    """Display the contact page"""
    return HttpResponse("this is contact page")