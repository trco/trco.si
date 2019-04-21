from django.urls import reverse_lazy
from django.views import generic

from .forms import BookForm
from .models import Book
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)


class Dbmf(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dbmf/dbmf.html'


class BookCreateView(BSModalCreateView):
    template_name = 'dbmf/create_book.html'
    form_class = BookForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('dbmf:dbmf')


class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'dbmf/update_book.html'
    form_class = BookForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('dbmf:dbmf')


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'dbmf/read_book.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'dbmf/delete_book.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('dbmf:dbmf')
