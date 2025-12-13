"""Определяет схемы URL для ппользователей"""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Добавить URL авторризации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистации.
    path('register/', views.register, name='register'),
]