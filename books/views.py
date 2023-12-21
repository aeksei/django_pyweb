from django.shortcuts import render

from . import models


def home(request):
    context = {
        "books_list": models.books,
        "categories": models.categories_data,
    }
    return render(request, "books/home.html", context=context)


def about(request):
    context = {
        "categories": models.categories_data,
    }
    return render(request, "books/about.html", context=context)


def book_detail(request, book_id):
    book = models.get_book_or_404(models.books, book_id)
    context = {
        "book": book,
        "categories": models.categories_data,
    }
    return render(request, "books/book_detail.html", context=context)


def category_books(request, category_slug):
    books_list = [book for book in models.books if book["category"] == category_slug]
    context = {
        "books_list": books_list,
        "categories": models.categories_data,
    }
    return render(request, "books/category_books.html", context=context)