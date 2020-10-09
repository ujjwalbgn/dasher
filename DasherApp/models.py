from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [('In Progress', 'In Progress'), ('Completed', 'Completed')]

    title = models.CharField(max_length= 200, null= True)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,null=True)
    assignto =  models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.title