from django.db import models
from django.utils.timezone import now

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

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, default='Unknown')
    city = models.CharField(max_length=100, default='Unknown')
    languages = models.TextField(default='Unknown')
    visit_time = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"Visitor from {self.ip_address} at {self.visit_time}"


