from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.university.api.v1.urls')),
]
