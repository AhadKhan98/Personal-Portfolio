from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    skills = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
