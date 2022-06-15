from django.shortcuts import render
from django.conf import settings
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


# Create your views here.
from django.views.generic.base import TemplateView

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY

        return context


