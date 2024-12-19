from django.contrib import admin

from lists.models import Task, SubTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list_type', 'due_date', 'display', 'total_subtasks')
    search_fields = ('title', 'list_type')


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'completed')
    search_fields = ('title', 'task__title')
    list_filter = ('completed',)
