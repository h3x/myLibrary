from django.db import models
from django.template.defaultfilters import slugify


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    city_id = models.ForeignKey(City,models.CASCADE)
    country_id = models.ForeignKey(Country,models.CASCADE)

    def __str__(self):
        return f"{self.city_id},{self.country_id}"


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50) # TODO: Slug field should be unique
    author_id = models.ForeignKey(Author, models.CASCADE)
    location_id = models.ForeignKey(Location, models.CASCADE)
    tag_ids = models.ManyToManyField(Tag, blank=True)
    isbn = models.CharField(max_length=20)
    date_edition = models.DateField()
    edition = models.IntegerField()

    # TODO: In here ensure that slug field in unique, if not, make it unique before saving
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}:{self.author_id} ({self.location_id})"
