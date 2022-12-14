from django.db import models
from django.contrib import admin
# Create your models here.

class Players(models.Model):
    jerseynumber=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    strikerate=models.FloatField()
    runs=models.IntegerField()

class PlayersAdmin(admin.ModelAdmin):
    list_display=('jerseynumber','name','age','strikerate','runs')
# Create your models here.
