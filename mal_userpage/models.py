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
