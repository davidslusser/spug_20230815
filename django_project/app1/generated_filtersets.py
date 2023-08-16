""" filtersets for applicable app models """

from rest_framework_filters.filters import RelatedFilter, BooleanFilter
from rest_framework_filters.filterset import FilterSet

# import models
from app1.models import (Brand,
                         Manufacturer,
                         Product
                         )


class BrandFilterSet(FilterSet):
    """filterset class for Brand"""
    manufacturer = RelatedFilter('ManufacturerFilterSet', field_name='manufacturer', queryset=Manufacturer.objects.all())
    product = RelatedFilter('ProductFilterSet', field_name='product', queryset=Product.objects.all())
    has_product = BooleanFilter(field_name='product', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Brand
        fields = {
            'created_at': '__all__',        
            'enabled': '__all__',        
            'id': '__all__',        
            'manufacturer': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class ManufacturerFilterSet(FilterSet):
    """filterset class for Manufacturer"""
    brand = RelatedFilter('BrandFilterSet', field_name='brand', queryset=Brand.objects.all())
    has_brand = BooleanFilter(field_name='brand', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Manufacturer
        fields = {
            'created_at': '__all__',        
            'enabled': '__all__',        
            'id': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class ProductFilterSet(FilterSet):
    """filterset class for Product"""
    brand = RelatedFilter('BrandFilterSet', field_name='brand', queryset=Brand.objects.all())

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Product
        fields = {
            'brand': '__all__',        
            'created_at': '__all__',        
            'description': '__all__',        
            'enabled': '__all__',        
            'sku': '__all__',        
            'updated_at': '__all__',        
        }
        