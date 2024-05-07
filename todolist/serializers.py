from rest_framework import serializers
from .models import ToDoList, ToDoItem


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["id", "title"]


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ["id", "title", "description", "created_date", "todo_list"]
