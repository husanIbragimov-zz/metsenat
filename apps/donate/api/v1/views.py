from rest_framework import generics, status
from rest_framework.response import Response

from apps.donate.models import Donate
from .serializers import DonateSerializer


class DonateListAPIView(generics.ListAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer


class DonateRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer


class DonateCreateAPIView(generics.CreateAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     sponsor = self.request.user
    #     value = sponsor.sponsor_wallet - sponsor.donates.donate
    #     serializer.save(sponsor=sponsor, sponsor_wallet=value)
