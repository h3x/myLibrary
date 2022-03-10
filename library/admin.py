import django.contrib.admin
from django.contrib import admin
from .models import Location,Author,City,Country,Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_id', 'date_edition', 'edition', 'location_id')
    list_filter = ('location_id','author_id')


# Register your models here.
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Book,BookAdmin)