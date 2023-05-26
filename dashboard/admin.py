from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(theatre_manager)
class theatre_managerModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "address", "phone"]
    
@admin.register(theatre)
class theatreModelAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "address", "theatre_manager"]
    
@admin.register(screen)
class screenModelAdmin(admin.ModelAdmin):
    list_display = ["name", "no_of_rows", "no_of_columns", "theatre"]
    
@admin.register(movie)
class movieModelAdmin(admin.ModelAdmin):
    list_display = ["name", "hero", "heroine", "director", "genre", "language", "description", "release_date","runtime_in_minutes", "trailer","thumbnail_image","slideshow_image"]
    
@admin.register(show)
class showModelAdmin(admin.ModelAdmin):
    list_display = ["date", "time", "price", "screen", "theatre", "movie"]