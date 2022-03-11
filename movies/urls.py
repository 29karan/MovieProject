from nturl2path import url2pathname
from django import urls


from django.urls import path
from .views import movie_detail, movies_list, search_view
app_name = 'movies'

urlpatterns = [
    path('', movies_list, name='list'),
    path('<int:id>/', movie_detail, name='movie_detail'),
    path('search/', search_view, name="search")
]
