from django.contrib import admin
from searchsite.models import Library
from searchsite.models import Book
from searchsite.models import Author
from searchsite.models import Librarian
from searchsite.models import Checks_Out
from searchsite.models import User
from searchsite.models import Publisher
from searchsite.models import Librarian_Genre
from searchsite.models import Library_Books
from searchsite.models import Written_By

# Register your models here.
admin.site.register(User)
admin.site.register(Checks_Out)
admin.site.register(Written_By)
admin.site.register(Library_Books)
admin.site.register(Librarian_Genre)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Publisher)
