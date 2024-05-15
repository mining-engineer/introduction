from django.db import models
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название группы'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')
        ordering = ['name']


class Soloists(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Имя солиста'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Солист')
        verbose_name_plural = _('Солисты')
        ordering = ['name']


class Performances(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название выступления'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Выступление')
        verbose_name_plural = _('Выступления')
        ordering = ['title']


class Schedules(models.Model):
    ORDER_CHOICES = [(i, str(i)) for i in range(1, 100)]  # Предопределенные значения для номера по порядку

    number = models.IntegerField(choices=ORDER_CHOICES, verbose_name=_('Номер по порядку'))
    performance = models.ForeignKey(Performances, on_delete=models.CASCADE, verbose_name=_('Выступление'))
    solist = models.ManyToManyField(Soloists, related_name='schedules', blank=True, verbose_name=_('Солисты'))
    group = models.ManyToManyField(Group, related_name='schedules', blank=True, verbose_name=_('Группы'))
    is_published = models.BooleanField(default=True, verbose_name=_('Опубликовано'))

    def __str__(self):
        return f'{self.number} - {self.performance.title}'

    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')
        ordering = ['number']