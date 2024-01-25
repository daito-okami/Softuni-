from django.urls import path

from petstagramm.common.views import index

urlpatterns = [
    path("", index, name="index")
]