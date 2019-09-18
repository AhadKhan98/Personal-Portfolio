from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    skills = models.CharField(max_length=50)
    description = models.TextField()
    githuburl = models.CharField(max_length=200)

class Job(models.Model):
    title = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.TextField()

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/certificates/')
    summary = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title
