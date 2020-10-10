from django.forms import ModelForm

from .models import *
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'