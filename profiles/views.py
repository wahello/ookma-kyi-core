from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from profiles.forms import UpdateNotificationPreferenceForm

# Create your views here.
@login_required
def profile_view(request):
    """View function for user profiles."""
    user = request.user
    return render(request, 'profiles/profile.html', context={'user': user})


@login_required
def update_notification_preference_view(request):
    """View function for user to change email."""
    if request.method == "POST":
        form = UpdateNotificationPreferenceForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/profile/")
    else:
        form = UpdateNotificationPreferenceForm(instance=request.user.profile)
        return render(request, "profiles/update_notification_preference_form.html", {'form': form})
