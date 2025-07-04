from .models import Books
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import  filters

from .pagination import BooksPagination
from .permission import IsSuperAdmin
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = BooksPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'author': ['exact'],
        'publish_year': ['exact'],
    }
    ordering_fields = ['title', 'publish_year', 'author']  # Поля для сортировки


    def get_permissions(self):

        if self.action in ['create', 'destroy']:
            permission_classes = [IsSuperAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]