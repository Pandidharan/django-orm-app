from django.contrib import admin

from .models import Players,PlayersAdmin
# Register your models here.

admin.site.register(Players,PlayersAdmin)
