from django.shortcuts import render
from rest_framework import viewsets
from .serializers  import NotesSerializer, CategorySerializer
from .models import Note, Category
 
class NotesViewSet(viewsets.ModelViewSet):
    query = Note.objects.all()
    serializer_class = NotesSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    query = Category.objects.all()
    serializer_class = CategorySerializer    

