from django.contrib import admin

from main_app.models import Employee

# Register your models here.
class EmploteeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmploteeAdmin)