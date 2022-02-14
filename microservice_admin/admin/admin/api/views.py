import random
import requests
import json
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductSerializer, ProductUserSerializer
from .models import Product, ProductUser

from .producer import publish


# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductLikeViewSet(viewsets.ViewSet):
    def like(self, request, pk):
        req = requests.get('http://host.docker.internal:8002/api/user')
        user_id = int(req.json()['id'])
        try:
            data = {"user_id":user_id, "product_id":pk}
            serializer = ProductUserSerializer(data = data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print("Product liked id:" + pk)
            publish('product_liked', pk)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        except:
            return Response({"message":"You already liked the pproduct"}, status= status.HTTP_400_BAD_REQUEST)
        