
from django.contrib import admin
from django.urls import path, include

from djangoProject.cities.views import index, list_phones, create_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_person, name="create person"),
    path('cities/', include('djangoProject.cities.urls')),
    path('', include('djangoProject.people.urls')),

    # path('citis/', index),
    # path('cities/phones', list_phones)
]
