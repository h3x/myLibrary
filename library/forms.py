from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author_id',
            'location_id',
            'tag_ids',
            'isbn',
            'date_edition',
            'edition',
        ]