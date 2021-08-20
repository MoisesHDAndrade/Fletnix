from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q
from django.core.files import File
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from django.http import HttpResponse

from Fletnix.apps.core.imdb import search_imdb, get_cover
from Fletnix.apps.profiles.models import WhoIsWatching
from .models import Movies
from .forms import MoviesForm
from .serializers import MoviesSerializer

from bs4 import BeautifulSoup as bs
import requests
from urllib import request as req
from tempfile import NamedTemporaryFile

import json

lista = []

class MoviesAddApiView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

@method_decorator(login_required, name = 'dispatch')
class MovieIndexView(ListView):
    model = Movies
    context_object_name = 'movies'
    template_name = 'index_movie.html'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user = self.request.user)
        if not qs:
            return qs
        return qs


    def get_context_data(self):
        context = super().get_context_data()
        context['recents'] = Movies.objects.filter(user = self.request.user).order_by('-id')[:7]
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
    if request.method == 'POST':
        form = MoviesForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data_from_form = Movies(
                user = request.user,
                title = form.cleaned_data['title'],
                summary = form.cleaned_data['summary'],
                year = form.cleaned_data['year'],
                genre = form.cleaned_data['genre'],
                cover = form.cleaned_data['cover'],
                url = form.cleaned_data['url'],
                trailer = form.cleaned_data['trailer'],
                cast = form.cleaned_data['cast'],
                image = form.cleaned_data['image'],
                certification = form.cleaned_data['certification'],
                relevance = form.cleaned_data['relevance']

            )
            if not data_from_form.image:
                striped_image = str(data_from_form.cover).split('/')
                image_url = data_from_form.cover
                img_temp = NamedTemporaryFile(delete = True)
                img_temp.write(req.urlopen(image_url).read())
                img_temp.flush()
                data_from_form.image.save(striped_image[-1], File(img_temp))
            
            data_from_form.genre = data_from_form.genre[0:-1]
            if not "iframe" or not "youtube" in data_from_form.url:
                data_from_form.url = "{sources: [{src:'url' ,type: 'video/mp4'}],poster: 'image'},".replace('url', data_from_form.url).replace('image', data_from_form.image.url)
            data_from_form.user = request.user
            if not data_from_form.trailer:
                data_from_form.trailer = 'https://www.youtube.com/watch?v=trailer'
            if not data_from_form.cast:
                data_from_form.cast = 'Information not available'
            data_from_form.save()
            messages.success(request, f'Yay! "{data_from_form.title}" was added to your library')
            return redirect('movies:index')
        if form.errors:
            print(form.errors)
    return render(request, 'movie_info.html', {'form':form})


def save_titles(request):
    movies = Movies.objects.all()
    movie_list = []
    for movie in movies:
        movie_dict = {"title":movie.title, "url":movie.url}
        movie_list.append(movie_dict)
        # print(f'{movie.title} {movie.url}')
      
    with open('titles_saved.json','w') as file:
        teste = json.dump(movie_list, file)
    return HttpResponse(movies)




###############################################################################################

def search_from_my_server(request, search):

    dicionario = dict()
    global lista
    lista = []
    res = search_imdb(search, request.user.user_profile.user_language)
  
    if len(list(res)) > 0:
        return res
    else:
        movie_less_last = search.strip(".mp4")[:-1]
        last_char = search.strip(".mp4")[-1]
        fixed_name = f'{movie_less_last} {last_char}'
        return search_imdb(fixed_name, request.user.user_profile.user_language)
        



def scrape_from_server(request):
    req = requests.get('http://192.168.1.18/Filmes/')
    soup = bs(req.text, 'html.parser')
    movie_link = soup.find_all('a')
    for link in movie_link:
        if 'href' in link.attrs and  'mp4' in link.attrs['href']:
            res = search_from_my_server(request, link.text.strip('.mp4'))
            item = list(res)
            print(item)
            # sliced = str(list(res).img).split('"')
            # print(sliced)
            
    # print(movie_link)
    return HttpResponse(req)