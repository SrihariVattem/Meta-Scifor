from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_age = models.IntegerField()
    emp_role=models.CharField(max_length=100)
    emp_salary=models.IntegerField()
    emp_company=models.TextField(max_length=100)
    def __str__(self):
        return str(self.emp_name)
