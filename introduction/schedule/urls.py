from django.urls import path
from . import views

app_name: str = 'schedule'

urlpatterns: list = [
    path('', views.schedule_list, name='schedule_list'),
]