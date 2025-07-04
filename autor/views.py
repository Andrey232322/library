from .models import Author
from rest_framework.viewsets import ModelViewSet

from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer