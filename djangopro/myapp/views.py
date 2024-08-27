from django.shortcuts import render
from .models import AboutContent, Project, Skill, Visitor
from .utils import get_client_ip
from django.utils.translation import get_language
from django.utils import timezone

def index(request):
    # الحصول على عنوان IP
    ip_address = get_client_ip(request)

    # الحصول على محتوى 'About Me' والمشاريع والمهارات
    try:
        about_content = AboutContent.objects.first()
        projects = Project.objects.all()
        skills = Skill.objects.all()
    except AboutContent.DoesNotExist:
        about_content = None
        projects = []
        skills = []

    # تسجيل زيارة جديدة
    country_name = "Unknown"
    city_name = "Unknown"

    # سجل الزيارة في قاعدة البيانات
    Visitor.objects.create(
        ip_address=ip_address,
        country_name=country_name,
        city_name=city_name,
        ui_languages=get_language() or "Unknown",
        visit_time=timezone.now()
    )
    
    # حساب عدد الزوار
    visitor_count = Visitor.objects.count()

    context = {
        'about_content': about_content,
        'projects': projects,
        'skills': skills,
        'visitor_count': visitor_count,
    }

    return render(request, 'index.html', context)
