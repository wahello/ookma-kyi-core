from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from profiles.forms import UpdateNotificationPreferenceForm


# Create your views here.
def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, 'profiles/signup_form.html', {'form': form})


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
