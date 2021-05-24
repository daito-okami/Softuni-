from django.shortcuts import render

from djangoProject.cities.models import Person


def index(req):
    context = {'name': 'Daito',
               'people':Person.objects.all(),
    }
    return render(req, 'index.html', context)