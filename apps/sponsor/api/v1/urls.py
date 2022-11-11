from django.urls import path

from .views import SponsorWalletListAPIView, SponsorWalletRetrieveAPIView, SponsorWalletCreateAPIView

urlpatterns = [
    path('create/', SponsorWalletCreateAPIView.as_view()),
    path('list/', SponsorWalletListAPIView.as_view()),
    path('retrieve/<int:pk>/', SponsorWalletRetrieveAPIView.as_view()),
]
