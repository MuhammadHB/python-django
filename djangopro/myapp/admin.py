# admin.py
from django.contrib import admin
from .models import AboutContent, Project, Skill

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('content',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
