from django.db import models

# Create your models here.


class music_model(models.Model):
    song_name = models.CharField(max_length=255)
    song = models.FileField(upload_to="music")
    def __str__(self) -> str:
        return self.song_name