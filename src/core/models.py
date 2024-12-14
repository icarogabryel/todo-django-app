from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    color = models.CharField(max_length=10, default='#FFFFFF')
