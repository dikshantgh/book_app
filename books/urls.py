# books/urls.py

"""this is the url route for app named books"""
from django.urls import path

from books import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('detail/<uuid:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.SearchResultListView.as_view(), name='search_results'),

]