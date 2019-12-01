from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book, Author, Librarian, Checks_Out

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def libraries(request):
    all = Library.objects.all()
    out = ""
    for each in all:
        out += str(each)+"\n"
    return HttpResponse(out)


def books(request):
    return HttpResponse("Hello, I'm a book.")
