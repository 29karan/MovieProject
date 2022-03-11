from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def movies_list(request):
    """
    Returns movie list.
    """
    if request.method == 'GET':
        order_by = request.GET.get('order_by')
        if order_by is None:
            order_by = 'id'
        movies = Movie.objects.all().order_by(order_by)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_detail(request, id):
    """
    returns detail of specific movie.
    """
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def search_view(request):
    """
    Returns items after searching.
    """
    query = request.GET.get('query')
    movies = Movie.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)