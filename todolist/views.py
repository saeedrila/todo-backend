from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import ToDoList, ToDoItem
from .serializers import ToDoListSerializer, ToDoItemSerializer


# Pagination class
class ToDoListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 100


# ViewSet for ToDoList
class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    pagination_class = ToDoListPagination


# Filter class for ToDoItem
class ToDoItemFilter(filters.FilterSet):
    class Meta:
        model = ToDoItem
        fields = ["title", "description", "created_date", "todo_list"]


# ViewSet for ToDoItem
class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    pagination_class = ToDoListPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ToDoItemFilter
