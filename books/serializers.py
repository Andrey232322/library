from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    #author = serializers.CharField(source='author.full_name')
    class Meta:
        model = Books
        fields = ['id', 'author', 'title', 'publish_year', 'preface', 'cover']