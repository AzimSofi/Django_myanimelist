from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Anime
from .models import Manga
from .models import AnimeStats
from .models import MangaStats
from .models import UserAnimeScore
from .models import UserMangaScore



def index(request):
    animes = Anime.objects.all()
    mangas = Manga.objects.all()
    
    current_user = request.user
    animestats = AnimeStats.objects.get(user=current_user)
    mangastats = MangaStats.objects.get(user=current_user)

    anime_user_scores = UserAnimeScore.objects.filter(user=current_user)
    manga_user_scores = UserMangaScore.objects.filter(user=current_user)

    anime_scores_dict = {score.anime.id: score.score for score in anime_user_scores}
    manga_scores_dict = {score.manga.id: score.score for score in manga_user_scores}
    
    animes_with_scores = []
    for anime in animes:
        score = anime_scores_dict.get(anime.id, '-')
        animes_with_scores.append({'anime': anime, 'score': score})
        
    mangas_with_scores = []
    for manga in mangas:
        score = manga_scores_dict.get(manga.id, '-')
        mangas_with_scores.append({'manga': manga, 'score': score})
        
    context = {
        'animestats' : animestats,
        'mangastats' :mangastats,
        'animes_with_scores': animes_with_scores,
        'mangas_with_scores': mangas_with_scores,
    }
    
    return render(request, 'mal_userpage/index.html', context)