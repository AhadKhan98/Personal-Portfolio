from django.db import models

# Create your models here.
class Project(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=250)
