from django.db import models

# Create your models here.
class Company(models.Model):
    company_id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=200,choices = (('IT','IT'),
                                                      ('NON IT','NON IT'),
                                                      ('Consultancy','Consultancy'),
                                                      ))
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=10,blank=True)
    about = models.TextField(blank=True)
    choice = (('SDE1','SDE1'),('SDE2','SDE2'),('SDE3','SDE3'),('Manager','Manager'),('Product Manager','Product Manager'))
    position = models.CharField(max_length=50,choices=choice)

    # relationship many Employee to one company.
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

