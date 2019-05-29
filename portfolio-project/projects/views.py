from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.
def project(request):
    return render(request, 'projects/project.html')

def detail(request, project_id):
    proj_detail = get_object_or_404(Project,pk=project_id)
    return render(request, 'projects/detail.html', {'project':proj_detail})
