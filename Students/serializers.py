from .models import Task,Students_MarK
from rest_framework.serializers import ModelSerializer

class Task_Serializer(ModelSerializer):
    
    class Meta:
        model=Task
        fields="__all__"

class Students_mark_Serializer(ModelSerializer):
    class Meta:
        model=Students_MarK
        fields="__all__"

