from django.contrib import admin
from .models import Group, Soloists, Performances, Schedules


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('number', 'performance', 'solist', 'group', 'group_2', 'is_published')
    list_filter = ('is_published', 'performance', 'group', 'solist')
    search_fields = ['performance__title', 'solist__name', 'group__name']
    ordering = ['number']


admin.site.register(Group)
admin.site.register(Soloists)
admin.site.register(Performances)
admin.site.register(Schedules, SchedulesAdmin)