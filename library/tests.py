from django.test import TestCase
from .models import Book,Author,Tag,Location,City,Country


class PageTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'library/index.html')

    def test_single_book_page(self):
        response = self.client.get('/book/golden-son')
        self.assertTemplateUsed(response, 'library/single-book.html')


class BookTest(TestCase):
    def setUp(self):
        City.objects.create(name='Test City')
        Country.objects.create(name='Test Country')
        Author.objects.create(name="Test Author")
        city = City.objects.first()
        country = Country.objects.first()
        Location.objects.create(city_id=city, country_id=country)

        location = Location.objects.first()

        Author.objects.create(name="Test Author")
        author = Author.objects.first()
        Book.objects.create(title="Test Book",
                            location_id=location,
                            author_id=author,
                            isbn='123123',
                            date_edition='2022-01-01',
                            edition=22
                            )

    def test_book_exists(self):
        book = Book.objects.first()
        self.assertEqual(book.title, 'Test Book')

    def test_book_slug_created(self):
        book = Book.objects.first()
        self.assertEqual(book.slug, 'test-book')

    def test_city_exists(self):
        city = City.objects.first()
        self.assertEqual(city.name, 'Test City')

    def test_location_exists(self):
        location = Location.objects.first()
        self.assertEqual(location.city_id.name, 'Test City')

    def test_country_exists(self):
        country = Country.objects.first()
        self.assertEqual(country.name, 'Test Country')

    def test_author_exists(self):
        author = Author.objects.first()
        self.assertEqual(author.name, 'Test Author')
        