from django.contrib import admin
from .models import Group, Soloists, Performances, Schedules


from django.contrib import admin
from .models import Schedules

class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('number', 'performance_title', 'solist_names', 'group_names', 'is_published')
    list_filter = ('is_published', 'performance', 'group', 'solist')
    search_fields = ['performance__title', 'solist__name', 'group__name']
    ordering = ['number']
    change_form_template = 'admin/schedules/change_form.html'

admin.site.register(Schedules, SchedulesAdmin)


admin.site.register(Group)
admin.site.register(Soloists)
admin.site.register(Performances)
