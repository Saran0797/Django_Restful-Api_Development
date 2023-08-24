from django.urls import path
from backend import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('', views.item_get),
    # path('create/', views.item_post),
    # path('<int:pk>/delete/', views.item_delete),
    # path('<int:pk>/update/', views.item_update),
    path('token/', ObtainAuthToken.as_view())
]
