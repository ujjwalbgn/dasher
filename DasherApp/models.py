from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [('In Progress', 'In Progress'), ('Completed', 'Completed')]
    PRIORITY_CHOICES = [('High','High'),('Medium', 'Medium'),('Low','Low')]
    title = models.CharField(max_length= 200, null= True)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES,null=True)

    assignto = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.title


class Budget(models.Model):
    FIN_CHOICES = [('Income', 'Income'), ('Expenses', 'Expenses')]

    title = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=FIN_CHOICES,null=True)
    amount = models.DecimalField(blank=True, null=True,  max_digits=19, decimal_places=2)

    def __str__(self):
        return self.title