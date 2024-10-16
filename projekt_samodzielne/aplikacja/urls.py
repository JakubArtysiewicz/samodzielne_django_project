from django.urls import path
from .views import views_main
urlpatterns = [
    path('', views_main)
]