"""OokmaKyi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Use include() to add URLS from the applications and authentication system
from django.urls import include

# development use only
from django.conf import settings
from django.conf.urls.static import static

from pages.views import page_view
from profiles.views import signup_view

urlpatterns = [
    path('', page_view, name="site_index"),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/profile/', include('profiles.urls')),
    path('characters/', include('characters.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    # development use
