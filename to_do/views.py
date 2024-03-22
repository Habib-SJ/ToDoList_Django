from django.shortcuts import render, redirect
from .models import to_do
from django.contrib.auth.decorators import login_required
from .foms import TodoItemForm

# Create your views here.


def home_view(request):
    return render(request, 'to_do/home.html')


@login_required(login_url='/accounts/login')
def todo_list_view(request):
    user = request.user
    query = to_do.objects.filter(owner=user)
    #print(query.task)
    if request.method == 'POST':
        checked_list = request.POST.getlist('checked')
        checked_list = [int(i) for i in checked_list]
        for todo_item in query:
            if todo_item.id in checked_list:
                to_do.objects.filter(id=todo_item.id).update(checked=True)
            else:
                to_do.objects.filter(id=todo_item.id).update(checked=False)
        return redirect('/tasks')
    todo_list_len = len(query)
    return render(request, 'to_do/tasks_list.html', {'todolist': query,'todo_list_len':todo_list_len})

@login_required(login_url='/accounts/login')
def todo_item_create(request):
    user = request.user
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = user
            instance.save()
            print('task: ', instance)
            return redirect('todoapp:todo_list')

    form = TodoItemForm()

    return render(request, 'to_do/create_todo_item.html', {'form': form})


def todo_item_delete(request, id):
    try:
        item = to_do.objects.get(id=id)
    except:
        return redirect('todoapp:todo_list')

    if item.owner == request.user:
        item.delete()
        return redirect('todoapp:todo_list')
    else:
        return redirect('todoapp:todo_list')