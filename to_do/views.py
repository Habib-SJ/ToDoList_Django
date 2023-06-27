from django.shortcuts import render, redirect
from .models import to_do
from django.contrib.auth.decorators import login_required

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
        return redirect('/list/tasks')

    return render(request, 'to_do/tasks_list.html', {'todolist': query})

