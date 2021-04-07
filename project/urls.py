from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('home/', views.home, name='home'),
]