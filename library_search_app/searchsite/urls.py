from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index'),
    path('libraries/', views.libraries, name='libraries'),
    path('libraries/<libID>/', views.listBooksAt, name='booksAt'),
    path('search/', views.search, name='search'),
    path('search/<lbID>/', views.checkout, name='checkout'),
    path('librarians/', views.librarians, name='librarians'),
]
