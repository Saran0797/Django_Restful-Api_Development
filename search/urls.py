from django.urls import path
from search.views import SearchListOldView

from . import views

urlpatterns = [
    path('', views.SearchListOldView.as_view(), name='search')
]