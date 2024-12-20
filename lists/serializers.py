from rest_framework import serializers
from .models import Task, SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        exclude = ["id" ,"task"]


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True)
    completed_subtasks = serializers.IntegerField(read_only=True)
    total_subtasks = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)
        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        instance.title = validated_data.get('title', instance.title)
        instance.list_type = validated_data.get('list_type', instance.list_type)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.display = validated_data.get('display', instance.display)
        instance.save()

        # Update or create subtasks
        subtask_ids = [subtask['id'] for subtask in subtasks_data if 'id' in subtask]
        SubTask.objects.filter(task=instance).exclude(id__in=subtask_ids).delete()

        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id')
            if subtask_id:
                subtask = SubTask.objects.get(id=subtask_id, task=instance)
                subtask.title = subtask_data.get('title', subtask.title)
                subtask.completed = subtask_data.get('completed', subtask.completed)
                subtask.save()
            else:
                SubTask.objects.create(task=instance, **subtask_data)

        return instance

