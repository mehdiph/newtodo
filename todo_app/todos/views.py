from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .forms import TodoForm
from .models import Todo

# Create your views here.
def tasks(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:tasks')
    else:
        form = TodoForm()
    tasks = Todo.objects.all()

    for task in tasks:
        delta = task.due_date - timezone.now().date()
        delta = delta.days

        if delta < 0:
            task.status = 'overdue'
        elif delta == 0:
            task.status = 'in progress'
        elif delta == 1:
            task.status = 'tomorrow'
        elif 2 <= delta <= 7:
            task.status = 'next week'
        elif delta > 7:
            task.status = f"{delta} days left"

    return render(request, 'todos/index.html', {'form': form, 'tasks': tasks})


def task_done(request, id):
    task = get_object_or_404(Todo, id=id)
    task.is_done = not task.is_done
    task.save()
    return redirect('todos:tasks')