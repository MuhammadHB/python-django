# views.py
from django.shortcuts import render
from .models import AboutContent, Project, Skill

def index(request):
    about_content = AboutContent.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()

    context = {
        'about_content': about_content,
        'projects': projects,
        'skills': skills,
    }

    return render(request, 'index.html', context)
