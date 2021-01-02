from django.shortcuts import render,redirect, reverse
from . imdb import search_imdb, get_cover


lista = []

def index(request):
    search = ''
    dicionario = dict()
    global lista
    lista = []
    if request.method =='POST':
        search = request.POST.get('search')
    res = search_imdb(search)
    for item in res:
        dicionario = {'link':item.a.get('href'), 'text':item.text}
        lista.append(dicionario)
    return render(request, 'index.html', {'res':lista})


def cover(request,pk):
    global lista
    res = lista[pk -1]
    movie = get_cover(f"https://www.imdb.com/{res.get('link')}")
    return render(request, 'cover.html',{'res':movie})

