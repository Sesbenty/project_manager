# Generated by Django 4.2.1 on 2023-05-28 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_project_name_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='0d741dc696e94affbda93b47daf87248', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='board.project'),
            preserve_default=False,
        ),
    ]
