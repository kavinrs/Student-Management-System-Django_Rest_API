from .models import Task,Students_MarK,Student
from rest_framework.serializers import ModelSerializer

class Student_Serializer(ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class Task_Serializer(ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class Task_Data_Serializer(ModelSerializer):
    student_reference=Student_Serializer()
    class Meta:
        model=Task
        fields="__all__"

class Student_Task_Serializer(ModelSerializer):
    all_task=Task_Serializer(many=True)
    class Meta:
        model=Student
        fields="__all__"

class Students_mark_Serializer(ModelSerializer):

    class Meta:
        model=Students_MarK
        fields="__all__"

