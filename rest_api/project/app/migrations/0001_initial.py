# Generated by Django 5.1.2 on 2024-10-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_age', models.IntegerField()),
                ('emp_role', models.CharField(max_length=100)),
                ('emp_salary', models.IntegerField()),
                ('emp_company', models.TextField(max_length=100)),
            ],
        ),
    ]
