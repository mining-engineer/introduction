from django.contrib import admin
from .models import Group, Soloists, Performances, Schedules

admin.site.register(Group)
admin.site.register(Soloists)
admin.site.register(Performances)
admin.site.register(Schedules)