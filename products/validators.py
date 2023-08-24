from rest_framework import serializers
from products.models import Product
from rest_framework.validators import UniqueValidator


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        return serializers.ValidationError("This title is alredy exists")
    return value


unique_product_title = UniqueValidator(Product.objects.all(), lookup= "iexact")
