from django.urls import path

from .views import OTMListAPIView

urlpatterns = [
    path('otm/', OTMListAPIView.as_view()),
    # path('student-university/', StudentWalletListAPIView.as_view()),
    # path('student-university/<int:pk>/', StudentWalletRetrieveAPIView.as_view()),
    # path('sponsor-university/<int:pk>/', SponsorWalletRetrieveAPIView.as_view()),
    # path('sponsor-university/', SponsorWalletListAPIView.as_view()),
    # path('amount-spent/', AmountSpentListAPIView.as_view()),
    # path('amount-spent/<int:pk>/', AmountSpentRetrieveAPIView.as_view()),
]
