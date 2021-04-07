from django.utils import timezone
from django.contrib.auth.models import User
from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    project_title = models.CharField(max_length=100)
    design = models.TextField()
    userbility = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.project_title  
