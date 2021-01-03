from django.shortcuts import render,redirect, get_object_or_404
from Fletnix.apps.core.imdb import search_imdb, get_cover
from .models import Movies
from .forms import MoviesForm


lista = []



def movie_index(request):
    movies = Movies.objects.all()
    return render(request, 'index_movie.html', {'movies':movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk = pk)
    return render(request, 'movie_detail.html', {'obj':movie})

def movie_searcher(request):

    dicionario = dict()
    global lista
    lista = []
    if request.method =='POST':
        search = request.POST.get('search')
    res = search_imdb(search)
    print(res)
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