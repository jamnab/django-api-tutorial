from django.http import HttpResponse
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly

class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (IsAdminOrReadOnly, )

class ProductDetail(generics.RetrieveDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (IsAdminOrReadOnly, )

class ReviewList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (IsAdminOrReadOnly, )

  def perform_create(self, serializer):
    serializer.save(
      created_by=self.request.user,
      product_id=self.kwargs['pk'])