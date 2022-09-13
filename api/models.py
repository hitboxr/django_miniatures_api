from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail, Anchor


# Create your models here.


class Pack(models.Model):
    pack_name = models.CharField(max_length=100)
    pack_image = models.ImageField(upload_to='packs', unique=True, blank=True, null=True)
    pack_thumbnail = ImageSpecField(source='pack_image',
                                    processors=[Thumbnail(width=252, height=160, anchor=Anchor.BOTTOM)],
                                    format='PNG')
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pack_name']

    def __str__(self):
        return f'{self.pack_name} ({self.id})'


class Mini(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    pack = models.ForeignKey(Pack, related_name='minis', on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        # default to sorting by newest first
        ordering = ['-added']

    def __str__(self):
        return f'{self.name} ({self.id})'


class MiniImage(models.Model):
    mini = models.ForeignKey(Mini, related_name='mini_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='minis', unique=True)
