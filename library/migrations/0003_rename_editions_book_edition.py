# Generated by Django 4.0.3 on 2022-03-10 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_date_edition_book_editions_book_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='editions',
            new_name='edition',
        ),
    ]