from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.views import View

from donations.models import Institution, Donation, Category
from users.forms import RegistrationForm

User = get_user_model()


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


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'wolontariat/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            email = form.cleaned_data['email']
            # email = request.POST.get('email')
            # first_name = request.POST.get('first_name')
            # last_name = request.POST.get('last_name')
            # password = request.POST.get('password')
            # password2 = request.POST.get('password2')

            # if password == password2:
            #     CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            messages.success(request, "Konto zostało założone dla użytkownika " + email)
            return redirect('login')
        else:
            return render(request, 'wolontariat/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'wolontariat/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'wolontariat/register.html')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')

class DonationFormView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            categories = Category.objects.all()
            ctx = {'categories': categories}
            return render(request, 'wolontariat/form.html', ctx)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        pass

