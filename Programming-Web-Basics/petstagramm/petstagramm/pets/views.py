from django.shortcuts import render


def create_pet(request):
    context = {}

    return render(request, 'pets/create_pet.html', context=context)


def details_pet(request, username, pet_slug):
    context = {}

    return render(request, 'pets/details_pet.html', context=context)


def delete_pet(request, username, pet_slug):
    context = {}

    return render(request, 'pets/delete_pet.html', context=context)


def edit_pet(request, username, pet_slug):
    context = {}

    return render(request, 'pets/edit_pet.html', context=context)