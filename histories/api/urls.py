from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HistoriesView

router = DefaultRouter()
router.register("", HistoriesView, "histories")

urlpatterns = [
    path('', include(router.urls))
]
