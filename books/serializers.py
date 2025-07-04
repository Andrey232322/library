from rest_framework import serializers
from .models import Books
from autor.models import Author
from autor.serializers import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.full_name', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    class Meta:
        model = Books
        fields = ['id', 'author', 'title', 'publish_year', 'preface', 'cover', 'author_id']