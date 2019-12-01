from django.contrib import admin
from searchsite.models import Library
from searchsite.models import Book
from searchsite.models import Author
from searchsite.models import Librarian
from searchsite.models import Checks_Out
from searchsite.models import User


# Register your models here.
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Checks_Out)
admin.site.register(User)
