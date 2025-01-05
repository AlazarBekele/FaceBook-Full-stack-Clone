from django.db import models

# Create your models here.

class Story (models.Model):

    title = models.CharField (max_length=30)
    storyImage = models.ImageField (upload_to='')

    def __str__(self):
        return self.title

