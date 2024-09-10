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



# myapp/models.py


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    country_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    ui_languages = models.CharField(max_length=255)
    visit_time = models.DateTimeField()

    def __str__(self):
        return f"{self.ip_address} - {self.city_name}, {self.country_name}"









