from django.contrib import admin

from petstagramm.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)
class PetPhotoAdminAdmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'short_description', 'tagged_pets', 'link_to_pet')

    def short_description(self, obj):
        return obj.description[:15]

    def tagged_pets(self, obj):
        return ', '.join(pet.name for pet in obj.pets.all())

    def link_to_pet(self, obj):
        return u'<a href="/">%s</a>'.format(obj.pk)

    link_to_pet.allow_tags = True