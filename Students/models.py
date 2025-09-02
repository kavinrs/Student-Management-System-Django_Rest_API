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

class Students_MarK(models.Model):
    english_marks=models.IntegerField()
    maths_marks=models.IntegerField()
    science_marks=models.IntegerField()
    tamil_marks=models.IntegerField()
    social_marks=models.IntegerField()
    total=models.IntegerField()
    average=models.FloatField()
    score=models.BooleanField()

    
