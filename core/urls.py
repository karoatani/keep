from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("note", views.NoteViewset, basename="notes")
router.register("user", views.ModelViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
