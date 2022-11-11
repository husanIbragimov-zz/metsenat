from django.urls import path

from .views import AccountRegisterAPIView, AccountListAPIView, MyAccountAPIView, LoginAPIView

urlpatterns = [
    path('sign-up/', AccountRegisterAPIView.as_view()),
    path('sign-in/', LoginAPIView.as_view()),
    path('profiles/', AccountListAPIView.as_view()),
    path('profile/<str:phone>/', MyAccountAPIView.as_view()),
]
