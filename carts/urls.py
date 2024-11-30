from .views import CaratListView, CartCreateView
from django.urls import path

urlpatterns = [
    path('cart-list/', CaratListView.as_view(), name='cart_list'),
    path('cart-create/<slug:slug>/', CartCreateView.as_view(), name='cart_create'),
]

