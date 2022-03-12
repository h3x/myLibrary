from django.shortcuts import render
from .models import Book,Tag,Author
from django.core.exceptions import ObjectDoesNotExist


def index(req):
    vals = {}
    try:
        books = Book.objects.all()
        tags = Tag.objects.all()
        authors = Author.objects.all()
        vals.update({
            'books': books,
            'tags': tags,
            'authors': authors,
            'selected_tag': False
        })
    except ObjectDoesNotExist:
        pass

    return render(req, "library/index.html", vals)


def single_book(req, slug):
    vals = {}
    try:
        selected_book = Book.objects.get(slug=slug)
        vals.update({
            'book': selected_book,
            'tags': selected_book.tag_ids.all()
        })
    except ObjectDoesNotExist:
        pass
    return render(req, "library/single-book.html", vals)


# def books_filtered(req,tag=False, author=False):
#     vals = {
#         'selected_tag': False,
#         'selected_author': False
#     }
#     try:
#         vals.update({
#
#         })
#     except ObjectDoesNotExist:
#         pass
