from django.urls import path
from django.shortcuts import render
from todo_app.models import Task


def home_view(request):
    tasks = Task.objects.filter(is_completed=False).order_by("-updated_at")
    completed_task = Task.objects.filter(is_completed=True).order_by("-updated_at")

    context = {"tasks": tasks, "completed_task": completed_task}

    return render(request, "home_todo.html", context)


# def addTask(request):
#     return render(request, "addTask.html")
