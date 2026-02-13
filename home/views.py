from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        "variable":"hello this is a test variable",
        "variable2":"this is another test variable"
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("this is about page")
def services(request):
    return HttpResponse("this is services page")
def contact(request):
    return HttpResponse("this is contact page")