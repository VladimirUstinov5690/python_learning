from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('courses/', views.courses, name='courses'),
    path('courses/course_detail/', views.course_detail, name='course_detail'),
]