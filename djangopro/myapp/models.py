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


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    country_name = models.CharField(max_length=255, default='Unknown')
    city_name = models.CharField(max_length=255, default='Unknown')
    ui_languages = models.CharField(max_length=255, default='Unknown')
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.city_name}, {self.country_name}"









