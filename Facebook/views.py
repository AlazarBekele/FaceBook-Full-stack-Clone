from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import LogInput, Login_check
from django.contrib.auth import (
  authenticate,
  login,
  logout
)

# Create your views here.

# @login_required (login_url='login')

def index (request):

    return render (request, 'index.html')


def sign_up (request):

  sign = LogInput (request.POST or None)
  if request.method == 'POST':
    if sign.is_valid():

      sign.save()
      return redirect ('login')
    

  context = {
    'sign' : sign
  }

  return render (request, 'Sign.html', context=context)



def login_Page (request):

  log = Login_check(request.POST or None)

  if request.method == 'POST':
    if log.is_valid():

      username = log.cleaned_data.get('username')
      password = log.cleaned_data.get('password')

      user = authenticate (request, username=username, password=password)

      if user is not None:
        login (request, user)
        return redirect ('index')
      
  context = {
    'log' : log
  }

  return render (request, 'Login.html', context=context)