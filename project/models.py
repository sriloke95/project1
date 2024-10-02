from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    role=models.CharField(max_length=30)

    def __str__(self):
        return self.role

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.IntegerField()  # Add bonus field
    phone = models.CharField(max_length=15)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()


    def __str__(self):
        return self.first_name