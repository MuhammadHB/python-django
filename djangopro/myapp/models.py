# models.py
from django.db import models

class AboutContent(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Section"

class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
