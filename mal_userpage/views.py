from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Anime
from .models import Manga
from .models import AnimeStats
from .models import MangaStats

def index(request):
    animes = Anime.objects.all()
    mangas = Manga.objects.all()
    animestats = AnimeStats.objects.first() # 
    mangastats = MangaStats.objects.first() # 

    
    context = {
        'name': 'Sakurai',
        'animes': animes,
        'mangas': mangas,
        'animestats' : animestats,
        'mangastats' :mangastats,
    }
    
    return render(request, 'mal_userpage/index.html', context)