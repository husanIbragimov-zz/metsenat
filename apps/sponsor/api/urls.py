from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.sponsor.api.v1.urls'))
]
