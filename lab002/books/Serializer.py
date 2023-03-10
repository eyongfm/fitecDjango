from rest_framework import serializers

from lab002.books.models import Book 

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'description',
                  'author',
                  'price')
