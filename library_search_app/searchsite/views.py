from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Library, Book, Author, Librarian, Checks_Out, User
from .lib_forms import LoginForm

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
    try:
        if(request.POST['user_name']):
            name =request.POST['user_name']
            user = User.objects.newUser(name=name)
            return HttpResponseRedirect('index/')
    except KeyError:
        return render(request, 'login.html', context={})
    return render(request, 'login.html', context={})
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         user = User.objects.newUser(name=form.getData())
    #         return HttpResponseRedirect('/index/')
    # else:
    #     form = LoginForm()
    #
    # return render(request, 'login.html', {'form': form})

def index(request):
    return HttpResponse('Hello Worlddd')

def libraries(request):
    context = {
        'liblist': Library.objects.all()
    }
    return render(request, 'library_list.html', context)

def listBooksAt(request, libID):
    lib_instance = get_object_or_404(Library, pk=libID)
    books = Library_Books.objects.filter(library_name = libID)
    authors = {}
    for each in books:
        names = []
        ids = Written_By.objects.filter(book_ID=each.id)
        for author in ids:
            names.append(Author.objects.get(pk=author.id).name)
        authors.update({each.id: names})
    context = {
        'library': lib_instance,
        'books': books,
        'authors': authors,
    }
    return render(request, 'books_at.html', context)

def books(request):
    return HttpResponse("Hello, I'm a book.")
#
# def searchBook(request):
