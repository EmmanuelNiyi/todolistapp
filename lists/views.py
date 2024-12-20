from rest_framework import generics
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer


# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# SubTask Views
class SubTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = SubTaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return SubTask.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task = Task.objects.get(pk=self.kwargs['task_id'])
        serializer.save(task=task)


class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
