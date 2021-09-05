from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View

from donations.models import Institution, Donation
from users.forms import RegistrationForm



class LandingPage(View):
    def get(self, request):
        foundations = Institution.objects.filter(type=1)
        organisations = Institution.objects.filter(type=2)
        locals = Institution.objects.filter(type=3)
        bags_counter = Donation.objects.all().count()
        organisation_counter = Institution.objects.all().count()
        ctx = {'foundations': foundations, 'organisations': organisations, 'locals': locals,
               'bags_counter': bags_counter, 'organisation_counter': organisation_counter}
        return render(request, 'index.html', ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, 'wolontariat/form.html')


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'wolontariat/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            user_mail = form.cleaned_data['email']
            messages.success(request, "Konto zostało założone dla użytkownika " + user_mail)
            return redirect('login')
        else:
            return render(request, 'wolontariat/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'wolontariat/login.html' )

    def post(self, request):
        # form = LoginForm(request.POST)
        # if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return redirect('register')
        # else:
        #     return render(request, 'wolontariat/register.html', {'form': form})

