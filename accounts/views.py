from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView)

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('dbmf:dbmf')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('dbmf:dbmf')
