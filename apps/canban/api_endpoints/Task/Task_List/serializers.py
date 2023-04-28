from rest_framework.serializers import ModelSerializer

from apps.canban.models import Task


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', ]  # subtasks
        # todo Subtasks nested serializer
