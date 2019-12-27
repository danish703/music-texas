from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album/',blank=True,null=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Music(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='music/')
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.title