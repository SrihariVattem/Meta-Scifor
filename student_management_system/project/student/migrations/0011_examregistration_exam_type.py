# Generated by Django 5.1.4 on 2024-12-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='examregistration',
            name='exam_type',
            field=models.CharField(default='Unkown', max_length=100),
        ),
    ]