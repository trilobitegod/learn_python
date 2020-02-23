from django.urls import path
from assets import views


urlpatterns = [
    path('report/', views.report, name='report'),
]