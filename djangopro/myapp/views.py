from django.shortcuts import render
from .models import AboutContent, Project, Skill, Visitor
from .utils import get_client_ip, post_facebook_comment
from django.utils.translation import get_language
from django.utils import timezone
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    # الحصول على عنوان IP للعميل
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
    
    # نشر تعليق على Facebook (اختياري، يمكنك استخدامه حسب الحاجة)
    page_access_token = settings.FACEBOOK_APP_TOKEN
    post_id = 'your_facebook_post_id'  # قم بتحديثه بمعرف المنشور الفعلي
    message = 'Hello from Django!'  # قم بتحديث الرسالة حسب الحاجة

    try:
        success = post_facebook_comment(page_access_token, post_id, message)
        if success:
            logger.info("Successfully posted comment to Facebook.")
        else:
            logger.error("Failed to post comment to Facebook.")
    except Exception as e:
        logger.error(f"Error posting Facebook comment: {e}")

    # إعداد السياق للعرض
    context = {
        'about_content': about_content,
        'projects': projects,
        'skills': skills,
        'visitor_count': visitor_count,
    }

    return render(request, 'index.html', context)
