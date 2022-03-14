from django.shortcuts import render,redirect
from .models import Book, Tag, Author
from django.core.exceptions import ObjectDoesNotExist
from .forms import BookForm


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


def singleBook(req, slug):
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


def createBook(req):
    form = BookForm()
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('all-books')

    vals = {
        'form': form,
    }
    return render(req, "library/form-book.html", vals)


def updateBook(req, slug):
    vals = {}
    try:
        book = Book.objects.get(slug=slug)
        form = BookForm(instance=book)
        vals.update({
            'form':form,
        })
        if req.method == 'POST':
            form = BookForm(req.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('all-books')
        vals = {
            'form': form,
        }
    except ObjectDoesNotExist:
        return redirect('all-books')

    return render(req, "library/form-book.html", vals)


def deleteBook(req, slug):
    vals = {}
    try:
        selected_book = Book.objects.get(slug=slug)
        if req.method == "POST":
            selected_book.delete()
            return redirect('/')
        vals.update({
            'title': selected_book.title,
        })
    except ObjectDoesNotExist:
        return redirect('all-books')
    return render(req, "library/delete-object.html", vals)






# TODO: Should be able to filter books by tag or author
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
