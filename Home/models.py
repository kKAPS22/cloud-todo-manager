from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
import uuid
import os


def audio_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join("audio", f"{uuid.uuid4().hex}.{ext}")


def video_path(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join("video", f"{uuid.uuid4().hex}.{ext}")


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()

    audio = models.FileField(
        storage=default_storage,
        upload_to=audio_path,
        blank=True,
        null=True
    )

    video = models.FileField(
        storage=default_storage,
        upload_to=video_path,
        blank=True,
        null=True
    )

    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
