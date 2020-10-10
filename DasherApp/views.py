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

def allTask(request):
    # passing empty from
    taskForm = TaskForm()
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {'tasks': tasks,'taskForm' : taskForm}
        return render(request, 'DasherApp/allTask.html', context)


    # adding new task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Created')
            return HttpResponseRedirect(request.path_info)
        return render(request, 'DasherApp/allTask.html')

def task(request,pk):

    # passing empty from
    taskForm = TaskForm()

    task = Task.objects.get(id = pk)
    context = {'task': task, 'taskForm' : taskForm}
    if request.method == 'GET':
        return render(request, 'DasherApp/task.html', context)




def budget(request):
    if request.method == 'GET':
        return render(request, 'DasherApp/budget.html')

    if request.method == 'POST':
        return render(request, 'DasherApp/budget.html')