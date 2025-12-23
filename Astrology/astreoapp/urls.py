from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('horoscope/', views.horoscope, name='horoscope'),

    # Zodiac CRUD
    path('zodiacs/', views.zodiac_list, name='zodiac_list'),
    path('zodiacs/add/', views.zodiac_create, name='zodiac_create'),

    # Horoscope CRUD
    path('horoscopes/', views.horoscope_list, name='horoscope_list'),
    path('horoscopes/add/', views.horoscope_create, name='horoscope_create'),
]
