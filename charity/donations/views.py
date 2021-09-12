from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.views import View

from donations.models import Institution, Donation, Category
from users.forms import RegistrationForm, DonationForm
from users.models import CustomUser

User = get_user_model()


class LandingPage(View):
    def get(self, request):
        foundations = Institution.objects.filter(type=1)
        organisations = Institution.objects.filter(type=2)
        locals = Institution.objects.filter(type=3)

        donations = Donation.objects.filter(quantity__isnull=False)
        supported_organisations = Institution.objects.values('donation__institution_id').distinct().count() - 1

        total_bags = int(sum([int(donation.quantity) for donation in donations]) / 2)

        ctx = {'foundations': foundations, 'organisations': organisations, 'locals': locals,
               'total_bags': total_bags, 'supported_organisations': supported_organisations}

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
            institutions = Institution.objects.all()
            ctx = {'categories': categories, 'institutions': institutions}
            return render(request, 'wolontariat/form.html', ctx)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        quantity = request.POST.get('quantity')
        categories = request.POST.get('category')
        institution = request.POST.get('institution')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        pick_up_date = request.POST.get('pick_up_date')
        # pick_up_time = request.POST.get('pick_up_time')
        pick_up_comment = request.POST.get('pick_up_comment')
        user_id = request.user.id

        institution_to_add = Institution.objects.get(name=institution).id
        categories_to_add = Category.objects.get(name=categories)

        donation = Donation.objects.create(quantity=quantity, institution_id=institution_to_add, address=address,
                                           phone_number=phone_number, city=city,
                                           zip_code=zip_code, pick_up_date=pick_up_date,
                                           pick_up_comment=pick_up_comment, user_id=user_id)

        donation.categories.add(categories_to_add)
        donation.save()

        return render(request, 'wolontariat/form-confirmation.html')


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        donations = Donation.objects.filter(user_id=user_id)

        ctx = {'donations': donations}
        return render(request, 'wolontariat/user_profile.html', ctx)


class FormConfirmationView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'wolontariat/form-confirmation.html')
