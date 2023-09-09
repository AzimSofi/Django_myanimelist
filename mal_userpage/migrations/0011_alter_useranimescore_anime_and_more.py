# Generated by Django 4.2.4 on 2023-09-09 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mal_userpage', '0010_remove_anime_user_score_remove_manga_user_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranimescore',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mal_userpage.anime'),
        ),
        migrations.AlterField(
            model_name='useranimescore',
            name='score',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='useranimescore',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermangascore',
            name='manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mal_userpage.manga'),
        ),
        migrations.AlterField(
            model_name='usermangascore',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
