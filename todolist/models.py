from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "To Do List"
        verbose_name_plural = "To Do Lists"


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: created on {self.created_date}"

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Item"
        verbose_name_plural = "Items"
