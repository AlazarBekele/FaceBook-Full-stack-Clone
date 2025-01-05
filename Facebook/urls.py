from django.urls import path
from .views import index, login_Page, sign_up


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_Page, name='login'),
    path ('signup/', sign_up, name='signup')
]