from django import forms
from .models import Profile, SecureIDData, Story, ImageUpload, ProfileContainer, ProflieContainer2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (
  login, authenticate, logout
)


class LogInput (UserCreationForm):
      
      first_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'First Name',
         'autocomplate' : 'off'
      }))
      last_name = forms.CharField (max_length=30, widget = forms.TextInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'last Name',
         'autocomplate' : 'off'
      }))
      username = forms.CharField (widget = forms.TextInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter username',
         'autocomplate' : 'off'
      }))
      Email_Part= forms.EmailField (widget = forms.EmailInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter Email',
         'autocomplate' : 'off'
      }))
      password1 = forms.CharField (max_length=40, label='Password Confirm' , widget = forms.PasswordInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter Password1',
         'autocomplete': 'off'
      }))
      password2 = forms.CharField (max_length=40, label='Password Confirm', widget = forms.PasswordInput(attrs={
         'class' : 'form-control parkinsans',
         'placeholder' : 'Enter Password1',
         'autocomplete': 'off'
      }))

      class Meta:
          model = User
          fields = ('first_name', 'last_name', 'username', 'Email_Part', 'password1', 'password2')



class Login_check (forms.Form):

  username = forms.CharField (widget = forms.TextInput(attrs={
    'class' : 'form-control parkinsans',
    'placeholder' : 'User Name'

  }))

  password = forms.CharField (widget = forms.TextInput(attrs={
      
    'class' : 'form-control parkinsans',
    'placeholder' : 'Password',
    'type' : 'password'

  }))

  # Profile Token Container

class secureToken (forms.ModelForm):
    class Meta:
        
        model = SecureIDData
        fields = '__all__'

        widgets = {
            'Token' : forms.TextInput(attrs={
                'class' : 'form-control',
                'type' : 'text'
            }),
            'user_name' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'type' : 'password'
            })
        }


class postHouse (forms.ModelForm):
    class Meta:
        model = Story
        fields = '__all__'

        widgets = {
            'Story_owner' : forms.TextInput(attrs={
               'class' : 'form-control',               
            }),
            'About_story' : forms.TextInput(attrs={
               'class' : 'form-control',               
            })

        }


class ImageUploadForm (forms.ModelForm):
    class Meta:
        
        model = ImageUpload
        fields = ['title', 'image']



class CreateProfile (forms.ModelForm):
    class Meta:
        
        model = ProfileContainer
        fields = ['Profile_Picture', 'Name', 'LastName']

        widgets = {
            
         'Profile_Picture' : forms.ClearableFileInput(attrs={
             'class' : 'upload-icon'
         }),
            
         'Name' : forms.TextInput(attrs={
             'class' : 'form-control'
         }),

         'LastName' : forms.TextInput(attrs={
             'class' : 'form-control'
         }),

      }
        
        model = ProflieContainer2
        fields = ['Bio', 'Dob']

        widgets = {
            
         'Bio' : forms.Textarea(attrs={
             'class' : 'form-control',
             'id' : 'exampleFormControlTextarea1'
         }),

         'Dob' : forms.DateInput(attrs={
             'class' : 'form-control',
             'type' : 'date'
         })

        }
        

# class CreateProfile2 (forms.ModelForm):
#     class Meta:
        
        