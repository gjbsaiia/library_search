from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('allbooks/', views.books, name='books'),
    # path('$/', views.books, name='books'),
    path('libraries/', views.libraries, name='libraries'),
    path('libraries/booksAt/<libID>/', views.listBooksAt, name='booksAt')
    # path('$/', views.authors, name='authors'),
    # path('$/', views.librarians, name='librarians'),
    # path('$/', views.checked_out, name='checked out oooks'),
    # path('$/', views.users, name='users'),
]
