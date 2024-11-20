from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Tag

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    model = Task
    fields = ['content', 'deadline', 'is_done', 'tags']
    widgets = {
        'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }


# Task List View
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['is_done', '-created_at']


# Task Create View
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')


# Task Update View
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')


# Task Delete View
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
