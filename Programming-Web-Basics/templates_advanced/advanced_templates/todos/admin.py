from django.contrib import admin

from advanced_templates.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
