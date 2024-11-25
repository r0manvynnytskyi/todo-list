from django.utils import timezone
from django import forms
from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.content

    def is_overdue(self):
        if self.deadline and not self.is_done:
            return self.deadline < timezone.now()
        return False


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

