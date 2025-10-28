from django.http import HttpResponse
from rest_framework import generics, status, views
from rest_framework.response import Response
from django.db.models import Count, Q
from .models import Project, Task, Notification
from .serializers import ProjectSerializer, TaskSerializer, NotificationSerializer
from rest_framework import viewsets

import time
import math


from .tasks import notify_sending, heavy_computation

def notify_sending_view(request):
    # heavy_computation()
    result = notify_sending.delay(5, 7)
    result = {('asd','moh'):444}

    return HttpResponse(f'Result: {result.get(('asd','moh'))}')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related('owner').prefetch_related('tasks').annotate(
        task_count=Count('tasks'),
        completed_task_count=Count('tasks', filter=Q(tasks__completed=True))
    )
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('project', 'project__owner')
    serializer_class = TaskSerializer

class BulkCreateTasksView(views.APIView):
    """
    POST /tasks/bulk-create/
    [
        {"project": 1, "title": "Task 1", "description": "Desc"},
        {"project": 1, "title": "Task 2", "description": "Desc"},
    ]
    """
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        Task.objects.bulk_create([Task(**item) for item in serializer.validated_data])
        return Response({"status": "success", "message": "Tasks created successfully"}, status=status.HTTP_201_CREATED)


class BulkUpdateTasksView(views.APIView):
    """
    PUT /tasks/bulk-update/
    {
        "ids": [1, 2, 3],
        "completed": true
    }
    """
    def put(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        completed = request.data.get('completed', True)
        updated = Task.objects.filter(id__in=ids).update(completed=completed)
        return Response({"updated_count": updated})

class BulkDeleteTasksView(views.APIView):
    """
    DELETE /tasks/bulk-delete/
    {
        "ids": [1, 2, 3]
    }
    """
    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])
        deleted, _ = Task.objects.filter(id__in=ids).delete()
        return Response({"deleted_count": deleted})
