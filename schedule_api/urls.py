from rest_framework.routers import DefaultRouter

from schedule_api.views import  ClientViewSet

router = DefaultRouter()

# router.register("couches/", CouchViewSet)
router.register("clients", ClientViewSet)
# router.register("clubs/", SportClubViewSet)
# router.register("trainings/", TrainingsViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
