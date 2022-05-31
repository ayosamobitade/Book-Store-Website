from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

