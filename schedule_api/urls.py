from rest_framework.routers import SimpleRouter
from django.urls import path

from schedule_api.views import (ClientViewSet, CoachViewSet, SportClubViewSet,
                                TrainingDestroyAPIView, TrainingAPIView, ScheduleAPIView)

router = SimpleRouter()

router.register("coaches", CoachViewSet)
router.register("clients", ClientViewSet)
router.register("clubs", SportClubViewSet)


urlpatterns = [
    path("trainings/", TrainingAPIView.as_view()),
    path("trainings/<int:pk>", TrainingDestroyAPIView.as_view()),
    path("schedule/<int:id>", ScheduleAPIView.as_view())
]

urlpatterns.extend(router.urls)
