from rest_framework import viewsets
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductGenericViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
