from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoListViewSet, ToDoItemViewSet

router = DefaultRouter()
router.register(r"todolists", ToDoListViewSet)
router.register(r"todoitems", ToDoItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
