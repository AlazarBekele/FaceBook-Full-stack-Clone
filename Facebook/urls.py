from django.urls import path
from .views import index, login_page


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_page, name='login')
]