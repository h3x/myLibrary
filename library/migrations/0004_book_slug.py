# Generated by Django 4.0.3 on 2022-03-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_editions_book_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
