from .serializers import BookSerializer
from .models import Books
from .permission import IsPublisher
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters,viewsets
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response



class BookViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,IsPublisher]
    pagination_class=CustomPagination
    queryset=Books.objects.all()
    serializer_class=BookSerializer
    filter_backends=[filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields=['title','author']
    ordering_fields=['title']
    filterset_class=BookFilter
    
    if not serializer_class.validated_data:
        Response(serializer_class.errors)
