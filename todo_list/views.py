from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django import forms
from django.views import generic
from .models import Task, Tag
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request, 'index.html')


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)


    task.is_done = not task.is_done
    task.save()

    return redirect('task-list')


# Task Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'is_done', 'tags']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# Tag Form
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


# Task Views
class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['is_done', '-created_at']


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


# Tag Views
class TagListView(generic.ListView):
    model = Tag
    template_name = 'tags/tag_list.html'
    context_object_name = 'tags'
    ordering = ['name']


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tags/tag_form.html'
    success_url = reverse_lazy('tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tags/tag_form.html'
    success_url = reverse_lazy('tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'tags/tag_confirm_delete.html'
    success_url = reverse_lazy('tag-list')


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'tags/tag_detail.html'
    context_object_name = 'tag'


class CustomLogoutView(LogoutView):
    template_name = 'includes/logout.html'
    next_page = reverse_lazy('home')
