from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    skills = models.CharField(max_length=50)
    description = models.TextField()

class Job(models.Model):
    title = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.TextField()

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/certificates/')
    summary = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title
