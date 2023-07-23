from .serializers import BookSerializer
from .models import Books
from .permission import IsPublisher
from .filters import BookFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters,viewsets
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,IsPublisher]
    queryset=Books.objects.all()
    serializer_class=BookSerializer
    
    def get_queryset(self):
        self.filter_backends=[filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
        self.search_fields=['title','author']
        self.ordering_fields=['title']
        self.filterset_class=BookFilter
        return super().get_queryset()
    

     