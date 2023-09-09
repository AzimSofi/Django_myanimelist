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

    # 1. UserAnimeScoreから現在のユーザーに関連するスコアをすべて取得
    anime_user_scores = UserAnimeScore.objects.filter(user=current_user)
    manga_user_scores = UserMangaScore.objects.filter(user=current_user)

    # 2. これらのスコアをanime_idをキーとする辞書に変換
    anime_scores_dict = {score.anime.id: score.score for score in anime_user_scores}
    manga_scores_dict = {score.manga.id: score.score for score in manga_user_scores}
    
    context = {
        'name': 'Sakurai',
        'animes': animes,
        'mangas': mangas,
        'animestats' : animestats,
        'mangastats' :mangastats,
        'animescore' : anime_scores_dict,
        'mangascore' : manga_scores_dict,
    }
    
    return render(request, 'mal_userpage/index.html', context)