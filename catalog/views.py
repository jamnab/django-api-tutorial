from rest_framework import generics
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (IsAdminOrReadOnly, )
  lookup_url_kwarg = 'product_id'

class ProductDetail(generics.RetrieveDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = (IsAdminOrReadOnly, )
  lookup_url_kwarg = 'product_id'

class ReviewList(generics.ListCreateAPIView):
  serializer_class = ProductSerializer
  permission_classes = (IsAdminOrReadOnly, )
  lookup_url_kwarg = 'product_id'

  def perform_create(self, serializer):
    serializer.save(
      created_by=self.request.user,
      product_id=self.kwargs['product_id'])
  
  def get_queryset(self, serializer):
    product = self.kwargs['product_id']
    return Review.objects.filter(product_id=product)

class ReviewDetail(generics.RetrieveDestroyAPIView):
  serializer_class = ReviewSerializer
  permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
  lookup_url_kwarg = 'review_id'

  def get_queryset(self):
    review = self.kwargs['review_id']
    return Review.objects.filter(id=review)