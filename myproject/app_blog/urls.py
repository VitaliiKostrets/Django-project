from django.urls import path
from .views import HomePageView  # Використовуйте відносний імпорт

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Головна сторінка
]



#python manage.py runserver
