from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.downlaod_yt_video),
]
