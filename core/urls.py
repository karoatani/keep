from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("note", views.NoteViewset, basename="notes")

urlpatterns = [
    path("", include(router.urls)),
    # path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    # path("", include("social_django.urls", namespace="social")),
]
