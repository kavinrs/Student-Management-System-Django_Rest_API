from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=10,default='A')

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name=models.CharField(max_length=100)
    description=models.TextField()

    
