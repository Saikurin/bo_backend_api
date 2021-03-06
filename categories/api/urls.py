from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoriesView

router = DefaultRouter()
router.register("", CategoriesView, "categories")

urlpatterns = [
    path('', include(router.urls))
]
