from django.urls import path
from .views import index, login_page, sign_up


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_page, name='login'),
    path ('signup/', sign_up, name='signup')
]