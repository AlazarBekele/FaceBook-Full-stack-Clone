from django.db import models

# Create your models here.

class Story (models.Model):

    Story_owner = models.CharField (max_length=20)
    About_story = models.CharField (max_length=20)
    created = models.DateTimeField (auto_now_add=True, auto_created=True)
    StoryIMG = models.FileField (upload_to='StoryIMG/',null=True, blank=True)

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
    

class ImageUpload(models.Model):

    title = models.CharField (max_length=100)
    image = models.ImageField (upload_to='Picture/')

    def __str__(self):
        return self.title
    

class ProfileContainer (models.Model):

    Profile_Picture = models.ImageField (upload_to='Profile_Image/',null=True , blank=True)
    Name = models.CharField (max_length=20)
    LastName = models.CharField (max_length=30)
    Dob = models.DateTimeField ()
    Bio = models.TextField ()

    def __str__(self):
        return self.Name + ' ' + self.LastName