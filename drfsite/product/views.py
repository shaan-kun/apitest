from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ShopProductsAPIView(ListAPIView):
    def get(self, request, pk):
        try:
            products = Product.objects.filter(shop_id=pk).values()
            products = list(products)

            if len(products) == 0:
                raise Exception

            return Response({'products': products})
        except Exception as e:
            return Response({'error': 'Вы что-то нажали и всё сломалось!'})


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
