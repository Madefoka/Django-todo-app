from . import views
from django.urls import path

urlpatterns = [
    # Add Task
    path("addTask/", views.addTask, name="addTask"),
    # Task done
    path("mark_as_done/<int:pk>/", views.mark_as_done, name="mark_as_done"),
    # Task Undone
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name="mark_as_undone"),
    # Edit task
    path("edit_task/<int:pk>/", views.edit_task, name="edit_task"),
    # Delete task
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
]
