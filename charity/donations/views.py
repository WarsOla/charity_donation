from django.shortcuts import render
from django.views import View

from donations.models import Institution, Donation


class LandingPage(View):
    def get(self, request):
        foundations = Institution.objects.filter(type=1)
        organisations = Institution.objects.filter(type=2)
        locals = Institution.objects.filter(type=3)
        bags_counter = Donation.objects.all().count()
        organisation_counter = Institution.objects.all().count()
        ctx = {'foundations': foundations, 'organisations': organisations, 'locals': locals, 'bags_counter': bags_counter, 'organisation_counter': organisation_counter}
        return render(request, 'index.html', ctx)

class AddDonation(View):
    def get(self, request):
        return render(request, 'wolontariat/form.html')

class Login(View):
    def get(self, request):
        return render(request, 'wolontariat/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'wolontariat/register.html')
    def post(self, request):
        return render(request, 'wolontariat/login.html')