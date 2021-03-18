from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-title")
    num_of_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {
        "books": books,
        "avg_rating": avg_rating,
        "no_of_books": num_of_books
    })


def book_details(request, slug):

    # * here we can use id or pk(primary key)
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book-detail.html',
                  {
                      "title": book.title,
                      "author": book.author,
                      "rating": book.rating,
                      "is_bestseller": book. is_best_selling
                  }
                  )
