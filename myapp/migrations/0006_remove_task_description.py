# Generated by Django 5.1.3 on 2025-01-17 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_project_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
