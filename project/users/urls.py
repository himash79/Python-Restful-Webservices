from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('fetch_users', views.fetch_users, name='fetch_users'),
    path('fetch_user/<str:id>', views.fetch_user, name='fetch_user'),
    path('save_user', views.save_user, name='save_user'),
    path('update_user/<str:id>', views.update_user, name='update_user'),
    path('delete_user/<str:id>', views.delete_user, name='delete_user'),
]