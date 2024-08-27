# views.py
from django.shortcuts import render
from .models import AboutContent, Project, Skill, Visitor

def index(request):
    about_content = AboutContent.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    visitor_count = Visitor.objects.count()

    context = {
        'about_content': about_content,
        'projects': projects,
        'skills': skills,
        'visitor_count': visitor_count,
    }

    return render(request, 'index.html', context)


