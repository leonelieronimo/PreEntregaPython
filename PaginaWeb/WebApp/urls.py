from django.urls import path
from WebApp import views    

urlpatterns = [
    path('test/', views.test),
]