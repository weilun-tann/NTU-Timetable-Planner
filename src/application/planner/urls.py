from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='home'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('timetable/', views.timetable, name='timetable'),
    path('search/', views.search, name='search'),
]
