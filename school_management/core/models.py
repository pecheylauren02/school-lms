from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.FloatField()
