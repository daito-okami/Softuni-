from django.shortcuts import render

# Create your views here.
def create_photo(request):
    context = {}
    return render(request, template_name='photos/create_photo.html', context=context)


def details_photo(request, pk):
    context = {}
    return render(request, template_name='photos/details_photo.html', context=context)


def edit_photo(request, pk):
    context = {}
    return render(request, template_name='photos/edit_photo.html', context=context)