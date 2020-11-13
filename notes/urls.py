from django.urls import include, path
from rest_framework import routers
from .views import NotesViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'notes', NotesViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]