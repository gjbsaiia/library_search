from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.books, name='books'),
    path('$/', views.books, name='books'),
    path('$/', views.libraries, name='libraries'),
    path('$/', views.authors, name='authors'),
    path('$/', views.librarians, name='librarians'),
    path('$/', views.checked_out, name='checked out oooks'),
    path('$/', views.users, name='users'),
]
