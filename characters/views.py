from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def character_list_view(request):
    user = request.user
    return render(request, 'characters/characters.html', context={'user': user})
