# Generated by Django 5.0 on 2024-01-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-11-20'),
            preserve_default=False,
        ),
    ]
