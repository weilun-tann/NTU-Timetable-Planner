from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginUser, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('timetable/', views.timetable, name='timetable'),
    path('timetable/alt_indexes/', views.alt_indexes, name='alt_indexes'),
    path('full_course_names/', views.get_full_course_names, name='full_course_names'),
    path('search/', views.search, name='search'),
    path('loading/', views.loading, name='loading'),
]
