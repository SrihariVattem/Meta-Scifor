# Generated by Django 5.1.4 on 2024-12-11 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
