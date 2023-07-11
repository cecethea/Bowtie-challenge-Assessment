from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

# External application routers
# ie: from app.urls import router as app_router

from . import views


class OptionalSlashDefaultRouter(DefaultRouter):
    """ Subclass of DefaultRouter to make the trailing slash optional """

    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'


# Create a router and register our viewsets with it.
router = OptionalSlashDefaultRouter()

# External workplace application
# ie: router.registry.extend(app_router.registry)

# Main application routes
router.register('doctor', views.DoctorViewSet, basename='doctor')
router.register('schedule', views.DoctorScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),  # includes router generated URL
]
