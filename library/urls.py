from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='all-books'),
    path('book/<str:slug>', views.singleBook, name='single-books'),
    path('create', views.createBook, name='create-book'),
    path('update/<str:slug>', views.updateBook, name='update-book'),
    path('delete/<str:slug>', views.deleteBook, name='delete-book'),
]
