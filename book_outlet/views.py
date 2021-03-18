from django.http.response import Http404
from django.shortcuts import get_object_or_404, render

from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        "books": books
    })


def book_details(request, id):

    # * here we can use id or pk(primary key)
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_outlet/book-detail.html',
                  {
                      "title": book.title,
                      "author": book.author,
                      "rating": book.rating,
                      "is_bestseller": book. is_best_selling
                  }
                  )
 