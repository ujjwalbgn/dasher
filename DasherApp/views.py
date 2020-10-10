from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'DasherApp/home.html')

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