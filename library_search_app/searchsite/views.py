from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Library, Book, Author, Librarian, Checks_Out
from .lib_forms import LoginForm
from django.template import loader

book_filters = [
    'library_name',
    'publisher_name',
    'book_title',
    'genre',
    'author_name',
    'date_published',
]

librarian_filters = [
    'librarian_name',
    'genre',
    'library_name',
]

checkout_filters = [
    'user_name',
    'book_name',
    'library_name',
    'due_date',
]

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.newUser(name=form.user_name)
            return HttpResponseRedirect('/index/')
    else:
        form = LoginForm()
    return render(request, 'templates/login.html', {'form': form})

def index(request):
    return HttpResponse('Hello Worlddd')

def libraries(request):
    template = loader.get_template("templates/library_list.html")
    context = {
        'liblist': Library.objects.all()
    }
    return HttpResponse(template.render(context, request))

def books(request):
    return HttpResponse("Hello, I'm a book.")
#
# def searchBook(request):
