from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import LogInput

# Create your views here.

# @login_required (login_url='login')

def index (request):

    return render (request, 'index.html')


def login_page (request):

    return render (request, 'Login.html')


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