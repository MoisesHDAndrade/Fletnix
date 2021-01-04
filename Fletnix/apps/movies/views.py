from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from Fletnix.apps.core.imdb import search_imdb, get_cover
from .models import Movies
from .forms import MoviesForm
from django.db.models import Q
import requests

lista = []


class MovieIndexView(ListView):
    model = Movies
    context_object_name = 'movies'
    template_name = 'index_movie.html'

class MovieSearchView(MovieIndexView):
    template_name = 'library_movie_search.html'

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
        res = search_imdb(search)
    for item in res:
        dicionario = {
            'link':item.a.get('href'), 
            'text':item.h2.text,
            # 'summary':item.p, 
            'summary':item.find(class_="overview").text, 
            'image':str(item.img)
            }
        lista.append(dicionario)
    # print(dicionario)
    return render(request, 'search_movie.html', {'res':lista})

def movie_info(request,pk):
    global lista
    res = lista[pk -1]
    movie = get_cover(f"https://www.themoviedb.org{res.get('link')}")
    return render(request, 'movie_info.html',{'res':movie})


def movie_add(request):
    form = MoviesForm()
    title_t = request.GET.get('title')
    print(title_t)
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
            return redirect('movies:index')
        else:
            print('form nao foi valido')
    return render(request, 'movie_info.html', {'form':form})





############# Scraping do IMDB ####################


# def movie_searcher(request):
#     search = ''
#     dicionario = dict()
#     global lista
#     lista = []
#     if request.method =='POST':
#         search = request.POST.get('search')
#     res = search_imdb(search)
#     for item in res:
#         dicionario = {'link':item.a.get('href'), 'text':item.text}
#         lista.append(dicionario)
#     return render(request, 'index.html', {'res':lista})


# def movie_info(request,pk):
#     global lista
#     res = lista[pk -1]
#     movie = get_cover(f"https://www.imdb.com/{res.get('link')}")
#     return render(request, 'search_movie.html',{'res':movie})