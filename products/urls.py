from django.urls import path
from products import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product-update"),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="product-delete"),
    path('', views.ProductListAPIView.as_view(), name="product-get"),
    path('create/', views.ProductCreateAPIView.as_view(), name="product-create"),
    path('listcreate/', views.ProductListCreateAPIView.as_view(), name="product-list-create"),
    path('mixin/', views.ProductMixinView.as_view(), name="product-get-retrieve"),
    path('mixin/<int:pk>/', views.ProductMixinView.as_view(), name='product-detail')
]


