# Generated by Django 4.2.4 on 2023-09-09 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mal_userpage', '0007_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]