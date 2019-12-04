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
        u = User.objects.filter(pk = request.session['user_id'])
        if(u):
            booksout = Checks_Out.objects.filter(user_ID=request.session['user_id'],)
            books_out = []
            for each in booksout:
                books_out.append([str(each), each.id])
            return render(request, 'login.html', {'form': '', "user_id": request.session['user_id'], "user_name": request.session['user_name'], "booksOut": books_out,})
        else:
            del(request.session['user_name'])
            del(request.session['user_id'])
            request.session.modified = True
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
        lbid = library_book.id
        book = each.book_ID
        publisher = book.publisher_ID
        wby = Written_By.objects.filter(book_ID=each.book_ID)
        authors = []
        for each in wby:
            authors.append(each.author_ID)
        organized.append([book, authors, publisher, library_book, lbid])
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
    results.append(["",""])
    if 'user_name' not in request.session:
        return render(request, 'login.html', {'form': form, "user_id": "", "user_name": "", "booksOut": [],})
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            results = []
            params = form.getData()
            books = runQuery(params)
            if books == -1:
                results.append(["Please enter some parameter.", ""])
            else:
                if not books:
                    results.append(["No books found. Sorry.", ""])
                else:
                    for book in books:
                        results.append([str(book), book.id])
            return render(request, 'search.html', {'form': form, 'results': results, 'user_id': request.session['user_id'], 'user_name': request.session['user_name'],})
    else:
        form = searchForm()

    return render(request, 'search.html', {'form': form, 'results': results, 'user_id': request.session['user_id'], 'user_name': request.session['user_name'],})

def runQuery(params):
    wereParams = False
    filter = ""
    books = ''
    if(params["book_title"]):
        books = Book.objects.filter(title=params["book_title"])
        wereParams = True
    if(params["genre"]):
        wereParams = True
        if books:
            books = books.filter(genre=params["genre"])
        else:
            books = Book.objects.filter(genre=params["genre"])
    if(params["date_published"]):
        wereParams = True
        if books:
            books = books.filter(datePublished=params["date_published"])
        else:
            books = Book.objects.filter(datePublished=params["date_published"])
    if(params["publisher_name"]):
        wereParams = True
        publisherIDs = Publisher.objects.filter(name=params["publisher_name"])
        if books:
            books = books.filter(publisher_ID__in=publisherIDs)
        else:
            books = Book.objects.filter(publisher_ID__in=publisherIDs)
    if(params["author_name"]):
        wereParams = True
        authorIDs = Author.objects.filter(name=params["author_name"])
        bookIDs = Written_By.objects.filter(author_ID__in=authorIDs)
        if books:
            books = books.filter(pk__in=bookIDs)
        else:
            books = Book.objects.filter(pk__in=bookIDs)
    if(params["library_name"]):
        wereParams = True
        if(books):
            lib_books = Library_Books.objects.filter(library_name = params["library_name"], book_ID__in=books)
        else:
            lib_books = Library_Books.objects.filter(library_name = params["library_name"])
    else:
        lib_books = Library_Books.objects.filter(book_ID__in=books)
    if wereParams:
        return lib_books
    else:
        return -1

def checkout(request, lbID):
    if 'user_name' not in request.session:
        return render(request, 'login.html', {'form': form, "user_id": "", "user_name": "", "booksOut": [],})
    book_instance = get_object_or_404(Library_Books, pk=lbID)
    result = ""
    if(book_instance.count > 0):
        query = User.objects.filter(pk=request.session["user_id"])
        checkedout = Checks_Out.objects.new_checkout(user=query[0], book=book_instance)
        result = str(checkedout)
    else:
        result = "BOOK CURRENTLY OUT OF STOCK"
    return render(request, "checkout.html", {"result": result, "user_id": request.session['user_id'], "user_name": request.session['user_name'],})

def returnBook(request, chID):
    if 'user_name' not in request.session:
        return render(request, 'login.html', {'form': form, "user_id": "", "user_name": "", "booksOut": [],})
    checked_out = get_object_or_404(Checks_Out, pk=chID)
    book = checked_out.book_ID
    bk = Library_Books.objects.filter(book_ID=checked_out.book_ID, library_name=checked_out.library_name)
    if(bk):
        bk[0].incCount()
        Checks_Out.objects.get(pk=chID).delete()
        return render(request, "return.html", {"result": True, "book": book, "user_id": request.session['user_id'], "user_name": request.session['user_name'],})
    else:
        return render(request, "return.html", {"result": False, "book": book, "user_id": request.session['user_id'], "user_name": request.session['user_name'],})
