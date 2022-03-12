from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='all-books'),
    path('book/<str:slug>', views.single_book, name='single-books'),
]
