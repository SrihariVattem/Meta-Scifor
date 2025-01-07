from django.db import models

# Create your models here.
class Startup_register(models.Model):
    company_name=models.CharField(max_length=100)
    company_type=models.CharField(max_length=100)
    size_of_company=models.IntegerField()
    def __str__(self):
        return str(self.company_name)
