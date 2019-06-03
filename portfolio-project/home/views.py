from django.shortcuts import render
from projects.models import Project
from projects.models import Job
from projects.models import Certificate


# Create your views here.
def home(request):
    projects = Project.objects
    jobs = Job.objects
    certificates = Certificate.objects
    return render(request, 'home/home.html', {'projects':projects,'jobs':jobs,'certificates':certificates})
