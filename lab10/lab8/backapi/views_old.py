from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from backapi.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Get All, Get by ID, Create, Update, Delete
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # (/api/categories/<id>/products/)
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    """
    Get All, Get by ID, Create, Update, Delete
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
