# Generated by Django 4.2.1 on 2023-05-26 13:45
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='Project', max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='Name', max_length=500),
        ),
    ]


