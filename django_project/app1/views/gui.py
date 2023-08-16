from django.shortcuts import render
from django.views.generic import DetailView, View

from handyhelpers.permissions import InAnyGroup
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView

# import models
from app1.models import (Brand, Manufacturer, Product)

# import forms
# from app1.forms import ()


class Index(HandyHelperIndexView):
    """render the app1 index page"""

    title = """App1"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/app1/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "Dashboard for App1 ",
        },
        {
            "url": "/app1/rest",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List RESTful APIs for App1",
        },
    ]
    protected_item_list = []
    protected_group_name = "admin"


class ListBrands(HandyHelperListPlusCreateAndFilterView):
    """list available Brand entries"""
    queryset = Brand.objects.all()
    title = "Brand"
    table = "app1/table/brands.htm"


class DetailBrand(DetailView):
    model = Brand
    template_name = 'app1/detail/brand.html'


# class ListMyModels(HandyHelperListPlusCreateAndFilterView):
#     """list available MyModel entries"""
#     queryset = MyModel.objects.all()
#     title = "MyModel"
#     table = "myapp/table/mymodels.htm"


# class DetailMyModel(DetailView):
#     model = MyModel
#     template_name = 'myapp/detail/mymodel.html'
