from django.db import models
from django.contrib import admin

class Group(models.Model):
    title = models.CharField(max_length=255)  # Название группы
    
    class Meta:
        verbose_name = "Группа"  # название на русском для одной группы
        verbose_name_plural = "Группы"  # название на русском для нескольких групп

    def __str__(self):
        return self.title

