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
    

class Schedules(models.Model):
    ORDER_CHOICES = [(i, str(i)) for i in range(1, 100)]  # Предопределенные значения для номера по порядку

    number = models.IntegerField(choices=ORDER_CHOICES, verbose_name='Номер по порядку')
    performance = models.ForeignKey(Performances, on_delete=models.CASCADE, verbose_name='Выступление')
    solist = models.ForeignKey(Soloists, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Солист')
    solist_2 = models.ForeignKey(Soloists, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Солист 2')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Группа')
    group_2 = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Группа 2')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.number} - {self.performance.title}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['number']