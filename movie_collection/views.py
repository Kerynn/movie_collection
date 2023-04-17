from django.http import HttpResponse
from django.shortcuts import render

data = {
  'movies': [
    {
      'id': 4,
      'title': 'Fantastic Mr. Fox',
      'year': 2009
    },
    {
      'id': 5,
      'title': 'The Life Aquatic with Steve Zissou',
      'year': 2004
    },
    {
      'id': 6,
      'title': 'The Royal Tenenbaums',
      'year': 2001
    }
  ]
}

def movies(request):
  return render(request, 'movies/movies.html', data)

def home(request):
  return HttpResponse('Home Page')