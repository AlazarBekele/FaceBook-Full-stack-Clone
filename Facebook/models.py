from django.db import models

# Create your models here.

class Story (models.Model):

    Story_owner = models.CharField (max_length=20)
    About_story = models.CharField (max_length=20)
    created = models.DateTimeField (auto_now_add=True, auto_created=True)
    Story = models.FileField (null=True, blank=True,upload_to='StoryIMG/')

    def __str__(self):
        return self.Story_owner
    
    
class SecureIDData (models.Model):

    Token = models.CharField (max_length=8)
    user_name = models.CharField (max_length=20)

    def __str__(self):
        return self.user_name
    

class Profile (models.Model):

    First_Name = models.CharField (max_length=15)
    Last_Name = models.CharField (max_length=20)
    Profile_Img = models.ImageField (upload_to='')
    Bio = models.CharField (max_length=100)
    Date = models.DateTimeField (auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.First_Name + self.Last_Name