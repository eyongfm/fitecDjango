from django.shortcuts import render
from lab002.books.Serializer import BookSerializer

from lab002.books.models import Book
from django.http.response import JsonResponse 
from rest_framework.parsers import JsonParser
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def book_liste(request):
    if request.method == 'GET':
        books = Book.objects.all()
        title = request.GET.get('title',None)
        if title is not None:
            books=books.filter(title__icontains=title)
        book_serializer = BookSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    elif request.method == 'POST':
        book_data = JsonParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)           


# Create your views here.
