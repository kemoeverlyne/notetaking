from rest_framework import serializers
from .models import Note, Category

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
      title = Note
      field = ['title', 'text', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        title = Category
        field = ['name']
      