from django import forms
from .models import Profile
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
    'placeholder' : 'Enter Your Email'

  }))

  password = forms.CharField (widget = forms.TextInput(attrs={
      
    'class' : 'form-control parkinsans',
    'placeholder' : 'Password'

  }))


class ProfileInsert (forms.ModelForm):
    
    model = Profile
    fields = '__all__'

    widget = {
        
      'First_Name' : forms.TextInput(attrs={
          'class' : 'form-control',
          'type' : 'text'
      }),
      'Last_Name' : forms.TextInput(attrs={
          'class' : 'form-control',
          'type' : 'text'
      }),
      'Profile_Img' : forms.ImageField(attrs={
          'class' : 'form-control',
          'type' : 'file'
      }),
      'Bio' : forms.TextInput(attrs={
          'class' : 'form-control',
          'type' : 'text'
      }),
      'Date' : forms.DateField(attrs={
          'class' : 'form-control',
          'type' : 'date'
      }),
    }