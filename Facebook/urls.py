from django.urls import path
from .views import (
    index,
    login_Page,
    sign_up,
    ProfileView,
    Token,
    postStory
)


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_Page, name='login'),
    path ('signup/', sign_up, name='signup'),
    path ('profile/<str:id>', ProfileView, name='profile'),
    path ('token/<str:tokenID>', Token, name='Token'),
    path ('story/', postStory, name='story')
]