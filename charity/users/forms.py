from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class RegistrationForm(CustomUserCreationForm):
    class Meta:
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields

# class LoginForm(CustomUserCreationForm):
#         class Meta:
#             model = CustomUser
#             fields = ('email', 'password')
#
#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         qs = CustomUser.objects.filter(email__iexact=email)
#         if not qs.exists():
#             raise forms.ValidationError("This is an invalid user")
#         return email