from django.conf import settings
from django.db import models
# import user
from django.contrib.auth import get_user_model

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="projects",)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks",)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({'done' if self.completed else 'pending'})"


class Notification(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="notifications",)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} at {self.creation_date}"
