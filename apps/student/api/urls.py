from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.student.api.v1.urls'))
]
