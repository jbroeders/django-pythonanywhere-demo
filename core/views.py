
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, Django on PythonAnywhere!</h1>")