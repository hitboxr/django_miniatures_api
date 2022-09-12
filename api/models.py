from django.db import models


# Create your models here.


class Mini(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['added']


class MiniImage(models.Model):
    mini = models.ForeignKey(Mini, related_name='mini_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='minis', unique=True)


class Pack(models.Model):
    pack_image = models.ImageField()
