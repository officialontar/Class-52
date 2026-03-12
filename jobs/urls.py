from django.urls import path
from . import views

urlpatterns = [
    path('create_new_jobs/', views.create_new_jobs, name='create_new_jobs'),
]