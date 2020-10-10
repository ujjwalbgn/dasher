from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('task/', views.task, name="task"),
    path('budget/', views.budget, name="budget"),

]