from django.contrib import admin
from .models import AboutContent, Project, Skill, Visitor

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('content',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'country', 'city', 'languages', 'visit_time')
    list_filter = ('country', 'city')
    search_fields = ('ip_address', 'country', 'city', 'languages')
