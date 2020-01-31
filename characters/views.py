from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from characters.forms import CreateCharacterForm


# Create your views here.
@login_required
def character_list_view(request):
    user = request.user
    return render(request, 'characters/characters.html', context={'user': user})


@login_required()
def create_character_view(request):
    """View function for user to create a character."""
    if request.method == "POST":
        form = CreateCharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return HttpResponseRedirect("/characters/")
    else:
        form = CreateCharacterForm()
        return render(request, "characters/create_character_form.html", {'form': form})
