from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Anime
from .models import Manga

def index(request):
    animes = Anime.objects.all()
    mangas = Manga.objects.all()
    
    context = {
        'name': 'Sakurai',
        'animes': animes,
        'mangas': mangas,
    }
    
    return render(request, 'mal_userpage/index.html', context)