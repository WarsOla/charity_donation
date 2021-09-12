"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from donations import views as ex_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', ex_views.LandingPage.as_view(), name='main'),
    path('adddonation/', ex_views.DonationFormView.as_view(), name='donation'),
    path('login/', ex_views.LoginView.as_view(), name='login'),
    path('logout/', ex_views.LogoutView.as_view(), name='logout'),
    path('register/', ex_views.RegistrationView.as_view(), name='register'),
    path('profile/', ex_views.UserProfileView.as_view(), name='user-profile'),
    path('adddonation/form-confirmation.html', ex_views.FormConfirmationView.as_view(), name='confirmation'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
