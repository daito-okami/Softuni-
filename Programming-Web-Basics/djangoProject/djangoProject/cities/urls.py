
#cities.urls
from django.urls import path
from django.views.generic import TemplateView

from djangoProject.cities.views import index, list_phones

urlpatterns = [
    path('', index),
    path('phones/', list_phones),
    path('phones2/', TemplateView.as_view(template_name='phones.html'))
]