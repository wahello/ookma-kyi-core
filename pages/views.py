from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Page


def page_view(request, slug="index"):
    """View function for home page of site."""
    if slug == "index":
        index_available = Page.objects.filter(slug='index').count()
        if index_available == 0:
            return render(request, 'pages/default.html')
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page.html', context={'page': page})
