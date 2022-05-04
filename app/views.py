from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
