from django.db import models


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


class Book(models.Model):
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(Author,models.CASCADE)
    location_id = models.ForeignKey(Location,models.CASCADE)
    isbn = models.CharField(max_length=20)
    date_edition = models.DateField()
    edition = models.IntegerField()

    def __str__(self):
        return f"{self.title}:{self.author_id} ({self.location_id})"
