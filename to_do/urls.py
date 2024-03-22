from django.urls import path
from .views import home_view, todo_list_view, todo_item_create, todo_item_delete


app_name = 'todoapp'
urlpatterns = [
    path('', home_view),
    path('tasks/', todo_list_view, name='todo_list'),
    path('create/', todo_item_create, name='todo_list_create'),
    path('<id>/delete/', todo_item_delete, name='todo_list_delete')
]