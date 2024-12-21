from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    list_type = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    display = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def completed_subtasks(self):
        return self.subtasks.filter(completed=True).count()

    def total_subtasks(self):
        return self.subtasks.count()


class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'Completed' if self.completed else 'Incomplete'})"