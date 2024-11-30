from django.urls import path
from users.views import UserCreateAPIView, UserConfirmationView, LoginAPIView

urlpatterns = [
    path('user/', UserCreateAPIView.as_view(), name='user'),
    path('user_login/', LoginAPIView.as_view(), name='user-login'),
    path('user_confirmation/', UserConfirmationView.as_view(), name='user-confirmation'),
]
