from rest_framework import generics

from apps.student.models import StudentWallet
from .serializers import StudentWalletSerializer


class StudentWalletListAPIView(generics.ListAPIView):
    queryset = StudentWallet.objects.all()
    serializer_class = StudentWalletSerializer


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = StudentWallet.objects.all()
    serializer_class = StudentWalletSerializer
