from django import template

from advanced_templates.todos.models import Todo

register = template.Library()


@register.simple_tag()
def todos_count():
    return Todo.objects.count()