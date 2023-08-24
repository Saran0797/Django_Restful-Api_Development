from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(["POST"])
def item_post(request, *args, **kwargs):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.data
        return Response(instance)


@api_view(["GET"])
def item_get(request, *args, **kwargs):
    instance = Product.objects.all()
    if instance:
        serializer = ProductSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(["DELETE"])
def item_delete(request, pk, *args, **kwargs):
    instance = Product.objects.get(pk=pk)
    if instance:
        instance.delete()
        return Response({"message": "item has been deleted"})
    return Response({"message": "item not available"})


@api_view(["PUT"])
def item_update(request, pk, *args, **kwargs):
    data = request.data
    instance = Product.objects.get(pk=pk)
    if instance:
        serializer = ProductSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"message": "item not available"}, status=400)
    return Response({"message": "item not available"}, status=400)
