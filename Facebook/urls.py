from django.urls import path
from .views import (
    index,
    login_Page,
    sign_up,
    ProfileView,
    Token,
    postStory,
    logout_session,
    createprofile
)


urlpatterns = [
    path ('', index, name='index'),
    path ('login/<int:ProID>/', login_Page, name='login'),
    path ('signup/', sign_up, name='signup'),
    path ('profile/', ProfileView, name='profile'),
    path ('token/<str:tokenID>', Token, name='Token'),
    path ('story/', postStory, name='story'),
    path ('login/', logout_session, name='logout'),
    path ('create/<str:id>/', createprofile, name='create')
]