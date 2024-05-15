# admin.py

from django.contrib import admin
from .models import Schedules, Performances, Soloists, Group
from .forms import SchedulesForm

class SchedulesAdmin(admin.ModelAdmin):
    form = SchedulesForm
    list_display = ('number', 'performance_title_display', 'solist_names_display', 'group_names_display')

    def performance_title_display(self, obj):
        return obj.performance.title

    def solist_names_display(self, obj):
        return ', '.join(solist.name for solist in obj.solist.all())

    def group_names_display(self, obj):
        return ', '.join(group.name for group in obj.group.all())

admin.site.register(Schedules, SchedulesAdmin)
admin.site.register(Group)
admin.site.register(Soloists)
admin.site.register(Performances)