from django.db import models

# Create your models here.
class Aadhar (models.Model):
    aadhar_no = models.IntegerField(unique = True)
    create_date = models.DateTimeField()
    create_by = models.CharField(max_length=50)

    def __str__(self):
        return str (self.aadhar_no)
    

class Student (models.Model):
    stu_name = models.CharField(max_length=50)
    stu_city =  models.CharField(max_length=50)
    stu_email = models.EmailField()
    aadhar_no = models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    def __str__(self):
        return self.stu_name
    