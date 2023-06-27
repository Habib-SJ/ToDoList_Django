from django.urls import path
from .views import home_view, todo_list_view


appname = 'to_do'
urlpatterns = [
    path('', home_view),
    path('list/tasks', todo_list_view, name='todo_list')
]