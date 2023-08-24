from rest_framework import routers
from products.viewsets import ProductViewSet, ProductGenericViewSet

router = routers.DefaultRouter()
router.register("products-abc", ProductViewSet, "Products")
router.register("productlist", ProductGenericViewSet, "Productsget")

urlpatterns = router.urls
