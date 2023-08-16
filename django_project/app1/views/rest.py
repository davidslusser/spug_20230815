""" DRF viewsets for applicable app models """

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded
from handyhelpers.drf_permissions import InAnyGroup

# import models
from app1.models import (Brand)

# import serializers
from app1.serializers import (BrandSerializer)

# import filtersets
from app1.filtersets import (BrandFilterSet)


from django.http import JsonResponse
from django.views.generic import View


class SimplestJson(View):
    def get(self, request, *arg, **kwargs):
        return JsonResponse({"msg": "this is a json message"})


class SimpleJson(View):
    def get(self, request, *arg, **kwargs):
        data = Brand.objects.all()
        dd = dict(data.values_list("id", "name"))
        return JsonResponse({"msg": "this is a json message", "data": dd})


class BrandViewSet(viewsets.ModelViewSet):
    model = Brand
    queryset = model.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilterSet

       # expandable_fields = {
       #     "manufacturer": "app1.serializers.ManufacturerSerializer",
       # }

