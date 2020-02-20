from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.test),
    path('html/', views.get_html),
    path('author/', views.get_author),
    path('form/', views.get_name),
    path('csv/', views.some_view_csv),
    path('pdf/', views.some_view_pdf),
]