from .serializers import PostSerializer
from .models import Books
from .permission import IsPublisher
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters,viewsets
from django_filters.rest_framework import DjangoFilterBackend

class PostView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,IsPublisher]
    queryset=Books.objects.all()
    serializer_class=PostSerializer
    filter_backends=[filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields=['title','author']
    ordering_fields=['title']
    filterset_class=BookFilter
