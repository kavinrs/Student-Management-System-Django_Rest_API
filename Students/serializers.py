from .models import Task
from rest_framework.serializers import ModelSerializer

class Task_Serializer(ModelSerializer):
    
    class Meta:
        model=Task
        fields="__all__"