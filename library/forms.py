from django.forms import ModelForm,CheckboxSelectMultiple,ModelMultipleChoiceField
from .models import Book,Tag


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author_id',
            'location_id',
            'isbn',
            'date_edition',
            'edition',
            'tag_ids',
        ]