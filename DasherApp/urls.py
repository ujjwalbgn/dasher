from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('task/<str:pk>/', views.task, name="task"),
    path('task/', views.allTask, name="allTask"),
    path('budget/', views.budget, name="budget"),

]