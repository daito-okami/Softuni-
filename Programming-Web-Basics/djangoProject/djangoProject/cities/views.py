from django.http import HttpResponse
from django.shortcuts import render

from djangoProject.cities.models import Person


def index(req):
    context = {'name': 'Daito',
               'people':Person.objects.all(),
    }
    return render(req, 'index.html', context)



def list_phones(request):
    context = {'phones': ['Galaxy s5000', 'Iphone 12', 'Huawei Y7 Prime', ], 'message': 'Phones list'}
    return render(request, 'phones.html', context)
    # return HttpResponse('Phones list')