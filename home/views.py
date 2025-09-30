from django.shortcuts import render
from projects.models import Project

def home_view(request):
    latest = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'home/home.html', {'projects': latest})
