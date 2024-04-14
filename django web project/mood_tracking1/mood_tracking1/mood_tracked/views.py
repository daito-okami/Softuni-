

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from mood_tracking1.mood_tracked.forms import ActivityForm
from mood_tracking1.mood_tracked.models import Activity, MOOD_CHOICES
from django.utils import timezone
@login_required
def create_activity(request):
    print("Incoming request headers:", request.META)
    if request.method == 'POST':
        print("POST request received")
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            print("AJAX request received")
            mood = request.POST.get('mood')
            print("Mood:", mood)
            print("Inside AJAX block but before 'if mood:' check")
            if mood:
                print("Mood is not empty, starting a new activity")

                # Logic to start a new activity:
                if not Activity.objects.filter(created_by=request.user, end_time=None).exists():
                    print("Creating a new activity")
                    Activity.objects.create(
                        created_by=request.user,
                        mood=mood,
                        start_time=timezone.now()
                    )
                    print("End of the 'if mood:' block")
                return JsonResponse({'success': True})
            else:
                print("Handling 'Change Mood' logic")
                current_activity = Activity.objects.filter(created_by=request.user, end_time=None).first()
                if current_activity:
                    print("Inside the 'if current_activity:' block")
                    current_activity.end_time = timezone.now()
                    current_activity.save()
                    print("Activity saved successfully")
                    return JsonResponse({'success': True})

        else:  # Handle regular form submission
            form = ActivityForm(request.POST)
            if form.is_valid():
                activity = form.save(commit=False)
                activity.created_by = request.user
                activity.save()
                return redirect('dashboard')

    else:  # GET request
        form = ActivityForm()
        previous_activities = Activity.objects.filter(created_by=request.user).order_by('-created_at')[:3]

        for activity in previous_activities:
            if activity.start_time and activity.end_time:
                duration = activity.end_time - activity.start_time
                activity.duration = duration

        context = {
            'form': form,
            'previous_activities': previous_activities,
            'MOOD_CHOICES': MOOD_CHOICES
        }
        return render(request, 'main/dashboard.html', context)