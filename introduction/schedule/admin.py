from django.contrib import admin
from .models import Group, Soloists, Performances, Schedules


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('number', 'performance_title', 'solist_names', 'group_names',  'is_published')
    list_filter = ('is_published', 'performance', 'group', 'solist')
    search_fields = ['performance__title', 'solist__name', 'group__name']
    ordering = ['number']

    def performance_title(self, obj):
        return obj.performance.title
    performance_title.short_description = 'Выступление'

    def solist_names(self, obj):
        return ', '.join([s.name for s in obj.solist.all()])
    solist_names.short_description = 'Солисты'

    def group_names(self, obj):
        return ', '.join([g.name for g in obj.group.all()])
    group_names.short_description = 'Группы'


admin.site.register(Schedules, SchedulesAdmin)


admin.site.register(Group)
admin.site.register(Soloists)
admin.site.register(Performances)
