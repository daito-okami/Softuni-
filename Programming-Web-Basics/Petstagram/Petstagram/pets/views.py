from django.shortcuts import render, redirect

from Petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        'pets': all_pets
               }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count()
    context = {
        'pet': pet
    }

    return render(request, 'pets/pet_detail.html', context)



def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet,
    )
    like.save()
    return redirect('like pet')