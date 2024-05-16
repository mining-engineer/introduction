# /introduction/schedule/viwes.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Schedules

def schedule_list(request):
    schedules = Schedules.objects.all()
    context = {'schedules': schedules}
    return render(request, 'pages/schedule.html', context)