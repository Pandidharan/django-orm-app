from django.db import models
from django.contrib import admin
# Create your models here.

class Players(models.Model):
    class Meta():
        permissions=(("view_coach","can view coach details."),
                     ("view_marks","can view player details"),)
        
    jerseynumber=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    strikerate=models.FloatField()
    runs=models.IntegerField()

class PlayersAdmin(admin.ModelAdmin):
    list_display=('jerseynumber','name','age','strikerate','runs')
# Create your models here.
