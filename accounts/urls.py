"""Определяет схемы URL для ппользователей"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Добавить URL авторризации по умолчанию.
    path('', include('django.contrib.auth.urls')),
]