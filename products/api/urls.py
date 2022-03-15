from django.conf.urls import include
from django.urls import path

from .views import ProductsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ProductsView, "products")

urlpatterns = [
    path('', include(router.urls))
]
