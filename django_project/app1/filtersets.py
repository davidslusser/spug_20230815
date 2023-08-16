""" filtersets for applicable app1 models """

from rest_framework_filters.filters import RelatedFilter, BooleanFilter
from rest_framework_filters.filterset import FilterSet

# import models
from app1.models import (Brand, Manufacturer, Product)


class BrandFilterSet(FilterSet):
    """filterset class for Brand"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Brand
        fields = {
            "created_at": "__all__",
            "enabled": "__all__",
            "id": "__all__",
            "name": "__all__",
            "updated_at": "__all__",
        }

