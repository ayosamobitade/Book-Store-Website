from django.urls import path
from .views import OrdersPageView, charge

urlpatterns = [
    path('', OrdersPageView.as_view(), name = 'order'),
    path('charge/', charge, name='charge' )
]

