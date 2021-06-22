from django.contrib import admin

# Register your models here.
from Petstagram.pets.models import Pet, Like

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age')
    sortable_by = ('name',)

    def likes_count(self, obj):
        return obj.like_sett.count()



admin.site.register(Pet, PetAdmin)
