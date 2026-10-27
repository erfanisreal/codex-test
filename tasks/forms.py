from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        labels = {'title': 'عنوان کار'}
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'یک کار جدید بنویس…', 'autofocus': True})}
