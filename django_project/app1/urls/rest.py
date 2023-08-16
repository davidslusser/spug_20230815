from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app1.views import rest

router = routers.DefaultRouter()


# app1 API Endpoints
router.register(r"brand", rest.BrandViewSet, "brand")


urlpatterns = [
    # API views
    path("rest/", include(router.urls)),
    path("simplest/", rest.SimplestJson.as_view(), name="simplest"),
    path("simple/", rest.SimpleJson.as_view(), name="simple"),


]
