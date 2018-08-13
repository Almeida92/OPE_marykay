from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'principal/index.html')

def login(request):
    return render(request, 'principal/login.html')

