from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('courses/', views.courses, name='courses'),
    path('console/', views.console, name='console'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/<int:slide_order>/', views.lesson_view,
         name='lesson_view'),
    
]