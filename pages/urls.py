# pages/urls.py
"""This is the section for app named pages. This contains all urls route via pages app"""
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),

]

# template_name = 'registration/login.html' for LoginView() in django
