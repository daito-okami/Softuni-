from django.urls import path

from advanced_templates.todos.views import list_todos, create_todo

urlpatterns = [
    path('', list_todos, name='list todos'),
    path('create/', create_todo, name='create todos')
]