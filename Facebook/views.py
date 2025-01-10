from django.shortcuts import render, redirect,HttpResponse
from .models import Profile, Story, ImageUpload, ProfileContainer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import LogInput, Login_check, postHouse, ImageUploadForm, CreateProfile
from django.contrib.auth import (
  authenticate,
  login,
  logout
)


# Create your views here.

@login_required (login_url='login')
def index (request):
    
    StoryUploadedImage = ImageUpload.objects.all()

    context = {
      'UploadedImage' : StoryUploadedImage
    }

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



def login_Page (request, ProID):

  log = Login_check(request.POST or None)

  if request.method == 'POST':
    if log.is_valid():

      username = log.cleaned_data.get('username')
      password = log.cleaned_data.get('password')

      user = authenticate (request, username=username, password=password)

      if user is not None:
        login (request, user)

        Data = ProfileContainer.objects.get(pk=ProID)
        
        if Data is not None:

          return redirect ('index')
    
        else:

          return HttpResponse ('Bad!!')

      
  context = {
    'log' : log,
    'ProID' : ProID
  }

  return render (request, 'Login.html', context=context)



@login_required (login_url='login')
def ProfileView (request,):

  return render (request, 'Profile.html')



@login_required (login_url='login')
def Token (request, tokenID):

  return render (request, 'Head/Token.html')



def postStory (request):

  post = postHouse (request.POST or None)
  if request.method == 'POST':
    if post.is_valid():

      post.save()
      post = postHouse()
      return redirect ('index')
    
  StoryData = Story.objects.all()

  context = {
    'post' : post,
    'StoryData' : StoryData
  }

  return render (request, 'Post/Story/post_story.html', context=context)



def upload_image (request):

  if request.method == 'POST':

    image = ImageUploadForm(request.POST, request.FILES
    )
    if image.is_valid():
      image.save()
      return redirect ('index')
    else:
      image = HttpResponse('Bad Request!!!!')

    context = {
      'image' : image
    }

    return render (request, 'Try.html', context=context)
  

def logout_session (request):
    
  logout(request)
  mess = messages.SUCCESS (request, 'Successfully logout!!')
  
  context = {
    'message' : mess
  }

  return render (request, 'logout.html', context=context)


 
def createprofile(request, id):

  # try:

  #   EditProfile = ProfileContainer.objects.get(pk=id)
  
  # except:

  #   HttpResponse (request, 'Bad Request!!')

  # EditProfile = ProfileContainer.objects.get(pk=id)

  create = CreateProfile (request.POST or None)

  if id == 'T4b!uP#6yD7l@Wz*9AqJp':

    id = 'T4b!uP#6yD7l@Wz*9AqJp'

  else:

    HttpResponse (request, 'Bad Request!!')
        

  if request.method == 'POST':
    if create.is_valid():

      create.save()
      messages.success (request, 'Successfully Update!!')

  context = {
    'create' : create,
    # 'EditProifile' : EditProfile,
    'id' : id
  }

  return render (request, 'createprofile.html', context=context)