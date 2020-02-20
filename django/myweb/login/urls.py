from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('register/', views.register),
    path('confirm/', views.user_confirm),
]