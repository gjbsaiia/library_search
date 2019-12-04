from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .lib_forms import LoginForm, searchForm

book_filters = [
    'library_name',
    'publisher_name',
    'book_title',
    'genre',
    'author_name',
    'date_published',
]

checkout_filters = [
    'user_name',
    'book_name',
    'library_name',
    'due_date',
]

# Create your views here.
def login(request):
    if 'user_name' in request.session:
        booksout = Checks_Out.objects.filter(user_ID=request.session['user_id'],)
        books_out = []
        for each in booksout:
            books_out.append(str(each))
        return render(request, 'login.html', {'form': '', "user_id": request.session['user_id'], "user_name": request.session['user_name'], "booksOut": books_out,})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.newUser(name=form.getData())
            request.session['user_name'] = user.name
            request.session['user_id'] = user.id
            request.session.modified = True
            booksout = Checks_Out.objects.filter(user_ID=request.session['user_id'],)
            books_out = []
            for each in booksout:
                books_out.append(str(each))
            return render(request, 'login.html', {'form': '', "user_id": request.session['user_id'], "user_name": request.session['user_name'], "booksOut": books_out,})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, "user_id": "", "user_name": "", "booksOut": [],})

def libraries(request):
    context = {
        'liblist': Library.objects.all()
    }
    return render(request, 'library_list.html', context)

def listBooksAt(request, libID):
    lib_instance = get_object_or_404(Library, pk=libID)
    books = Library_Books.objects.filter(library_name = libID)
    organized = []
    for each in books:
        names = []
        library_book = each
        book = each.book_ID
        publisher = book.publisher_ID
        wby = Written_By.objects.filter(book_ID=each.book_ID)
        authors = []
        for each in wby:
            authors.append(each.author_ID)
        organized.append([book, authors, publisher, library_book])
    context = {
        'library': lib_instance,
        'organized': organized,
    }
    return render(request, 'books_at.html', context)

def librarians(request):
    organized = []
    libs = Librarian.objects.all()
    for lib in libs:
        genre = Librarian_Genre.objects.filter(librarian_ID=lib)
        organized.append([lib.name, lib.getLibraryName(), genre])
    context = {
        'librarians': organized,
    }
    return render(request, "librarian_list.html", context)

def search(request):
    results = []
    bookIds = []
    if 'user_name' not in request.session:
        return HttpResponseRedirect('')
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            params = form.getData()
            books = runQuery(params)
            if not books:
                results = ["No books found. Sorry."]
            else:
                for book in books:
                    results.append(str(book))
                    bookIds.append(book.id)
            return render(request, 'search.html', {'form': form, 'bookIds': bookIds, 'results': results, 'user_id': request.session['user_id'], 'user_name': request.session['user_name'],})
    else:
        form = searchForm()

    return render(request, 'search.html', {'form': form, 'bookIds': bookIds, 'results': results, 'user_id': request.session['user_id'], 'user_name': request.session['user_name'],})

def runQuery(params):
    filter = ""
    books = ''
    if(params["book_title"]):
        books = Book.objects.filter(title=params["book_title"])
    if(params["genre"]):
        if books:
            books = books.filter(genre=params["genre"])
        else:
            books = Book.objects.filter(genre=params["genre"])
    if(params["date_published"]):
        if books:
            books = books.filter(datePublished=params["date_published"])
        else:
            books = Book.objects.filter(datePublished=params["date_published"])
    if(params["publisher_name"]):
        publisherIDs = Publisher.objects.filter(name=params["publisher_name"])
        if books:
            books = books.filter(publisher_ID__in=publisherIDs)
        else:
            books = Book.objects.filter(publisher_ID__in=publisherIDs)
    if(params["author_name"]):
        authorIDs = Author.objects.filter(name=params["author_name"])
        bookIDs = Written_By.objects.filter(author_ID__in=authorIDs)
        if books:
            books = books.filter(pk__in=bookIDs)
        else:
            books = Book.objects.filter(pk__in=bookIDs)
    if(params["library_name"]):
        if(books):
            lib_books = Library_Books.objects.filter(library_name = params["library_name"], book_ID__in=books)
        else:
            lib_books = Library_Books.objects.filter(library_name = params["library_name"])
    else:
        lib_books = Library_Books.objects.filter(book_ID__in=books)
    return lib_books

def checkout(request, lbID):
    if 'user_name' not in request.session:
        return HttpResponseRedirect('')
    book_instance = get_object_or_404(Library_Books, pk=lbID)
    result = ""
    if(book_instance.count > 0):
        checkedout = Checks_Out.objects.new_checkout(user=request.session["user_id"], book=book_instance.book_ID.id, library=book_instance.library_name.name)
        result = str(checkedout)
    else:
        result = "BOOK CURRENTLY OUT OF STOCK"
    return render(request, "checkout.html", {"result": result, "user_id": request.session['user_id'], "user_name": request.session['user_name'],})
