from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student,Task
from .serializers import Task_Serializer

class StudentList(APIView):
    def get(self,request):

        student_back=Student.objects.all()
        student_list=[]
        for i in student_back:
            stu_dic={
                "id":i.id,
                "name":i.name,
                "age":i.age,
                "grade":i.grade
            }
            student_list.append(stu_dic)
        return Response(student_list)
    def post(self,request):

        print(request.data)

        name=request.data["name"]
        age=request.data["age"]
        grade=request.data["grade"]
        student=Student(name=name,age=age,grade=grade)
        student.save()
        return Response("data added")
    
    def put(self,request,student_id):

        print(student_id,"Student ID")
        print(request)

        studunt_upd=Student.objects.filter(id=student_id)
        print(request.data)

        studunt_upd.update(name=request.data["name"],age=request.data["age"],grade=request.data["grade"])

        return Response("json updated")
    
    def delete(self,request,student_id):

        student_de=Student.objects.get(id=student_id)
        student_de.delete()
        return Response("Data Deleted")

class TaskList(APIView):
    def post(self,request):

        n_task=Task_Serializer(data=request.data)
        if n_task.is_valid():
            n_task.save()
            return Response("Task added")
        else:
            return Response(n_task.errors)
    def get(self,request):

        task=Task.objects.all()
        n_task=Task_Serializer(task,many=True).data

        return Response(n_task)
    
class TaskList_By_ID(APIView):

    def get(self,request,task_id):

        task=Task.objects.get(id=task_id)

        n_task=Task_Serializer(task).data

        return Response(n_task)
    
    def patch(self,requesrt,task_id):
        task=Task.objects.get(id=task_id)

        n_task=Task_Serializer(task,data=requesrt.data,partial=True)

        if n_task.is_valid():
            n_task.save()
            return Response("Task Updated")
        else:
            return Response(n_task.errors)
    def put(self,request,task_id):

        task=Task.objects.get(id=task_id)

        n_task=Task_Serializer(task,data=request.data,partial=True)

        if n_task.is_valid():
            n_task.save()
            return Response("Task Updated")
        else:
            return Response(n_task.errors)
        
    def delete(self,request,task_id):

        task=Task.objects.get(id=task_id)
        task.delete()

        return Response("Task Deleted Succesfully")

