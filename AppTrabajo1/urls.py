from django.urls import path
from . import views

app_name = 'AppTrabajo1'

urlpatterns = [
    path('home', views.home, name='home'),
    path('home/about', views.about, name='about'),
]