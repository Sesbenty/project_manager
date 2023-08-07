import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Task(models.Model):
    class boardNames(models.TextChoices):
        ToDo = 'Сделать'
        InProgress = 'В процессе'
        Review = 'На проверке'
        Done = 'Выполнено'
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                              related_name='tasks')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                            editable=False)
    name = models.CharField(max_length=500, default="Name")
    boardName = models.CharField(max_length=12, choices=boardNames.choices,
                                 default=boardNames.ToDo)
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('board.Project', on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='projects')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=500, default="Project")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return str(self.name)


'''
class TaskTime(models.Model):
    task = models.ForeignKey('board.Task', on_delete=models.CASCADE,
                              related_name='tasks_time')
    dataStart = models.DateTimeField(auto_now_add=True)
    dataEnd = models.DateTimeField(auto_now_add=True)
'''