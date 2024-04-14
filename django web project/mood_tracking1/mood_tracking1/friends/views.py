from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Friend

@login_required
def friend(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)

    return render(request, 'friend/friend.html', {'friend': friend})
@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            friend = Friend.objects.create(title=title, created_by=request.user)
            friend.members.add(request.user)
            friend.save()

            userprofile = request.user.userprofile
            userprofile.active_friend_id = friend.id
            userprofile.save()

            return redirect('account')

    return render(request, 'friend/add.html')

