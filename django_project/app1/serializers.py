""" DRF serailizers for applicable app1 models """

from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

# import models
from app1.models import (Brand, Manufacturer, Product)


class BrandSerializer(FlexFieldsModelSerializer):
    """serializer class for Brand"""
    manufacturer = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Brand
        fields = [
            "created_at",
            "enabled",
            "id",
            "name",
            "manufacturer",
            "updated_at",
        ]

        expandable_fields = {
            "manufacturer": "app1.serializers.ManufacturerSerializer",
        }



class ManufacturerSerializer(FlexFieldsModelSerializer):
    """serializer class for Manufacturer"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Manufacturer
        fields = [
            "created_at",
            "enabled",
            "id",
            "name",
            "updated_at",
        ]