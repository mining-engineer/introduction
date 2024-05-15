from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название группы')  # Название группы
    
    class Meta:
        verbose_name =  _("Группа")  # название на русском для одной группы
        verbose_name_plural = _("Группы")  # название на русском для нескольких групп

    def __str__(self):
        return self.title
    
    
class Soloists(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя солиста')  # Имя солиста
    
    class Meta:
        verbose_name =  _("Солист")  # название на русском для одного солиста
        verbose_name_plural = _("Солисты")  # название на русском для нескольких солистов

    def __str__(self):
        return self.title


class Performances(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование номера')
    
    class Meta:
        verbose_name =  _("Номер")
        verbose_name_plural = _("Номера")

    def __str__(self):
        return self.title