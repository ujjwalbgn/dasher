from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.

def home(request):

    tasks  = Task.objects.all()
    budgets = Budget.objects.all()

    context = {'tasks':tasks,'budgets': budgets}

    return render(request, 'DasherApp/main.html', context)

def task(request):
    if request.method == 'GET':
        return render(request, 'DasherApp/task.html')

    if request.method == 'POST':
        return render(request, 'DasherApp/task.html')


def budget(request):
    if request.method == 'GET':
        return render(request, 'DasherApp/budget.html')

    if request.method == 'POST':
        return render(request, 'DasherApp/budget.html')