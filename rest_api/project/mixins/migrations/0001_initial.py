# Generated by Django 5.1.2 on 2024-10-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startup_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_type', models.CharField(max_length=100)),
                ('size_of_company', models.IntegerField()),
            ],
        ),
    ]
