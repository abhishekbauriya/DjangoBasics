from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    developed_by = "Vibhu Duraji"
    mentors = [
       "Aniket",
       "Ashish",
       "Ram",
       "Shubham",
       "Lohit"
    ]

    context = {
        "devloper": developed_by,
        "mentors": mentors
    }

    response = render(request, 'HelloWorld/index.html', context)
    return response

def hello(request):
    return render(request, 'HelloWorld/hello.html')