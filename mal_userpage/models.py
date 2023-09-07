from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=255)
    picture_url = models.URLField(max_length=500)
    user_score = models.CharField()
    ep_watched = models.CharField()
    ep_total = models.CharField()

    def __str__(self):
        return self.name

class Manga(models.Model):
    name = models.CharField(max_length=255)
    picture_url = models.URLField(max_length=500)
    user_score = models.CharField()
    ch_read = models.CharField()
    ch_total = models.CharField()

    def __str__(self):
        return self.name

class AnimeStats(models.Model):
    Watching = models.IntegerField(default=0)
    Completed = models.IntegerField(default=0)
    OnHold = models.IntegerField(default=0)
    Dropped = models.IntegerField(default=0)
    PlanToWatch = models.IntegerField(default=0)
    TotalEntries = models.IntegerField(default=0)
    Rewatched = models.IntegerField(default=0)
    Episodes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class MangaStats(models.Model):
    Reading = models.IntegerField(default=0)
    Completed = models.IntegerField(default=0)
    OnHold = models.IntegerField(default=0)
    Dropped = models.IntegerField(default=0)
    PlanToWatch = models.IntegerField(default=0)
    TotalEntries = models.IntegerField(default=0)
    Reread = models.IntegerField(default=0)
    Chapters = models.IntegerField(default=0)
    Volumes = models.IntegerField(default=0)

    def __str__(self):
        return self.name