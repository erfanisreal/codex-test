from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from .forms import TaskForm
from .models import Task


@require_http_methods(['GET', 'POST'])
def index(request):
    form = TaskForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'tasks/index.html', {'form': form, 'tasks': Task.objects.order_by('-id')})


@require_POST
def toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save(update_fields=['completed'])
    return redirect('index')


@require_POST
def delete(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect('index')
