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

    return render(request, 'DasherApp/home.html', context)

def allTask(request):
    # passing empty from
    taskForm = TaskForm()
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {'tasks': tasks,'taskForm' : taskForm}
        return render(request, 'DasherApp/newTask.html', context)


    # adding new task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Created')
            return redirect('home')

def task(request,pk):

    # passing empty from
    taskForm = TaskForm()

    task = Task.objects.get(id = pk)
    context = {'task': task, 'taskForm' : taskForm}
    if request.method == 'GET':
        return render(request, 'DasherApp/task.html', context)




def allbudget(request):

    budgetForm = BudgetForm()

    if request.method == 'GET':

        budgets = Budget.objects.all()

        context = {'budgets': budgets, 'budgetForm': budgetForm}

        return render(request, 'DasherApp/inputBudget.html', context)

    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created')
            return redirect('home')

def deleteTask(request,pk):
    task = Task.objects.get(id = pk)

    if request.method == "POST":
        task.delete()
        return redirect('home')


def deleteBudget(request, pk):
    budget = Budget.objects.get(id=pk)

    if request.method == "POST":
        budget.delete()
        return redirect('home')