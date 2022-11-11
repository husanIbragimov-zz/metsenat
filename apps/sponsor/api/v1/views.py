from rest_framework import generics, status
from rest_framework.response import Response

from apps.account.api.v1.permissions import IsAuthenticated, IsOwnerOrReadOnlyForAccount
from apps.sponsor.models import SponsorWallet
from .serializers import SponsorWalletSerializer, SponsorCreateSerializer


class SponsorWalletCreateAPIView(generics.CreateAPIView):
    queryset = SponsorWallet.objects.all()
    serializer_class = SponsorCreateSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnlyForAccount)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()


class SponsorWalletListAPIView(generics.ListAPIView):
    queryset = SponsorWallet.objects.all()
    serializer_class = SponsorWalletSerializer


class SponsorWalletRetrieveAPIView(generics.RetrieveAPIView):
    queryset = SponsorWallet.objects.all()
    serializer_class = SponsorWalletSerializer
