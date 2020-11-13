from django.shortcuts import render
from rest_framework import viewsets
from .serializers  import NotesSerializer, CategorySerializer
from .models import Note, Category
 
class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    

