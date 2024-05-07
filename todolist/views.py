from rest_framework import viewsets
from .models import ToDoList, ToDoItem
from .serializers import ToDoListSerializer, ToDoItemSerializer

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer