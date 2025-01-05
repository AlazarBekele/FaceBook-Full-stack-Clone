from django.db import models

# Create your models here.

class Story (models.Model):

    Story_owner = models.CharField (max_length=20)
    About_story = models.CharField (max_length=20)
    Story = models.ImageField (upload_to='')

    def __str__(self):
        return self.Story_owner
    

class Profile (models.Model):

    First_Name = models.CharField (max_length=15)
    Last_Name = models.CharField (max_length=20)
    Profile_Img = models.ImageField (upload_to='')
    Bio = models.CharField (max_length=100)
    Date = models.DateField (auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.First_Name + self.Last_Name