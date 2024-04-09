from django.contrib import admin
from django.urls import path, include
from schedule_api.views import TrainingAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('schedule_api.urls')),
]
