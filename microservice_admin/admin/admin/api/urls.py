from django.contrib import admin
from django.urls import path


from .views import ProductViewSet, ProductLikeViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get':'list',
    })),
    path('products/<str:pk>/like', ProductLikeViewSet.as_view({
        'post':'like',
    })),
]