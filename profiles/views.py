from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def profile_view(request):
    """View function for user profiles."""
    user = request.user
    return render(request, 'profiles/profile.html', context={'user': user})