from django.urls import path
from .views import CustomLogoutView, TagDetailView
from .views import (
    index, toggle_task_status,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TagListView, TagCreateView, TagUpdateView, TagDeleteView,
)

app_name = 'todo'

urlpatterns = [

    path('', index, name='index'),

    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('task/add/', TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/toggle-status/', toggle_task_status, name='task-toggle-status'),

    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tag/add/', TagCreateView.as_view(), name='tag-add'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
