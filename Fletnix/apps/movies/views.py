from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q

from rest_framework import generics

from Fletnix.apps.core.imdb import search_imdb, get_cover
from Fletnix.apps.profiles.models import WhoIsWatching
from .models import Movies
from .forms import MoviesForm
from .serializers import MoviesSerializer

from bs4 import BeautifulSoup as bs
import requests

lista = []

class MoviesAddApiView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieIndexView(ListView):
    model = Movies
    context_object_name = 'movies'
    template_name = 'index_movie.html'
    paginate_by = 12

    def get_context_data(self):
        context = super().get_context_data()
        context['recents'] = Movies.objects.all().order_by('-id')[:7]
        context['watching'] = WhoIsWatching.objects.first()
        return context

class MovieSearchView(MovieIndexView):
    template_name = 'library_movie_search.html'
    paginate_by =  300
    def get_queryset(self):
        search = self.request.GET.get('search')
        qs = super().get_queryset()
        qs = qs.filter(
            Q(title__icontains = search) |
            Q(genre__icontains = search))
        if not search and not qs:
            return qs
        return qs
    
    

def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk = pk)
    return render(request, 'movie_detail.html', {'obj':movie})

def movie_searcher(request):
    res = ''
    dicionario = dict()
    global lista
    lista = []
    if request.method =='POST':
        search = request.POST.get('search')
        res = search_imdb(search, request.user.user_profile.user_language)
    for item in res:
        # print(item.find("img", class_="poster"))
        sliced = str(item.img).split('"')
        print(sliced)
        imagem = ''
        if len(sliced) > 1:
            imagem = sliced[7]
        else:
            imagem = None
        
        dicionario = {
            'link':item.a.get('href'), 
            'text':item.h2.text,
            'summary':item.find(class_="overview").text, 
            # 'image':str(item.img)
            'image':f'https://www.themoviedb.org{imagem}'
            }
        
        lista.append(dicionario)
    return render(request, 'search_movie.html', {'res':lista})

def movie_info(request,pk):
    global lista
    res = lista[pk -1]
    movie = get_cover(f"https://www.themoviedb.org{res.get('link')}")
    return render(request, 'movie_info.html',{'res':movie})


def movie_add(request):
    form = MoviesForm()
    title_t = request.GET.get('title')
    if request.method == 'POST':
        form = MoviesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data_from_form = Movies(
                title = form.cleaned_data['title'],
                summary = form.cleaned_data['summary'],
                year = form.cleaned_data['year'],
                genre = form.cleaned_data['genre'],
                cover = form.cleaned_data['cover'],
                url = form.cleaned_data['url'],
                trailer = form.cleaned_data['trailer'],
                cast = form.cleaned_data['cast']

            )
            data_from_form.genre = data_from_form.genre[0:-1]
            if not data_from_form.trailer:
                data_from_form.trailer = 'https://www.youtube.com/watch?v=trailer'
            if not data_from_form.cast:
                data_from_form.cast = 'Information not available'
            data_from_form.save()
            messages.success(request, f'Yay! "{data_from_form.title}" was added to your library')
            return redirect('movies:index')
        else:
            print('form nao foi valido')
    return render(request, 'movie_info.html', {'form':form})

