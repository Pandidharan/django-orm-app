# Generated by Django 3.2.5 on 2022-12-26 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricketplayersdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='players',
            options={'permissions': (('view_coach', 'can view coach details.'), ('view_marks', 'can view player details'))},
        ),
    ]
