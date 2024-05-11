from django.contrib import admin

# Register your models here.

from movies.models import Movies
admin.site.register(Movies)