from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def books(request):
    return HttpResponse("Hello, I'm a book.")
