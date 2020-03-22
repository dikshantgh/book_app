from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'  # default context_object_name = 'object_list'
    login_url = 'account_login' # if a non user tries to access the list directly then it redirects to login page


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book_object'  # default context_object_name = 'book' just lowercase the name of model
    login_url = 'account_login'


class SearchResultListView(ListView):
    model = Book
    # queryset = Book.search_book_object.all()
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):  # for search results
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

