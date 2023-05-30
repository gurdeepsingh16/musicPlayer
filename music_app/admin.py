from django.contrib import admin
from .models import music_model

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'song')
    list_filter = ('song_name',)
    list_per_page = 3
admin.site.register(music_model,ListingAdmin)
