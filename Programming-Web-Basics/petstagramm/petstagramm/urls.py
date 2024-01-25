
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagramm.common.urls')),
    path('accounts/', include('petstagramm.accounts.urls')),
    path('pets/', include('petstagramm.pets.urls')),
    path('photos/', include('petstagramm.photos.urls')),
]
