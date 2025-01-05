from django import forms
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


# class Story (forms.ModelForm):
    
#    class Meta:
       
#       model = 