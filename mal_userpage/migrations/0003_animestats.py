# Generated by Django 4.2.5 on 2023-09-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mal_userpage', '0002_manga'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
