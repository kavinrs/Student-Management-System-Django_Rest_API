from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

class StudentList(APIView):
    def get(self,request):

        # student_back=Student.objects.all()
        # student_list=[]
        # for i in student_back:
        #     stu_dic={
        #         "id":i.id,
        #         "name":i.name,
        #         "age":i.age,
        #         "grade":i.grade
        #     }
        #     student_list.append(stu_dic)
        # return Response(student_list)
        task=Student.objects.all()
        n_task=Student_Task_Serializer(task,many=True).data

        return Response(n_task)
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
    def get(self,request,task_id=None):

        if task_id==None:
            task=Task.objects.all()
            n_task=Task_Data_Serializer(task,many=True).data

            return Response(n_task)
        else:
            task=Task.objects.get(id=task_id)
            n_task=Task_Data_Serializer(task).data

            return Response(n_task)
    def patch(self,request,task_id):

        task=Task.objects.get(id=task_id)

        n_task=Task_Serializer(task,data=request.data,partial=True)

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
            return Response("n_task.errors")
    
    def delete(self,request,task_id):

        task=Task.objects.get(id=task_id)

        task.delete()

        return Response("Task Deleted Succesfully")
    
# class TaskList_By_ID(APIView):

#     def get(self,request,task_id):

#         task=Task.objects.get(id=task_id)

#         n_task=Task_Serializer(task).data

#         return Response(n_task)
    
#     def patch(self,requesrt,task_id):
#         task=Task.objects.get(id=task_id)

#         n_task=Task_Serializer(task,data=requesrt.data,partial=True)

#         if n_task.is_valid():
#             n_task.save()
#             return Response("Task Updated")
#         else:
#             return Response(n_task.errors)
#     def put(self,request,task_id):

#         task=Task.objects.get(id=task_id)

#         n_task=Task_Serializer(task,data=request.data,partial=True)

#         if n_task.is_valid():
#             n_task.save()
#             return Response("Task Updated")
#         else:
#             return Response(n_task.errors)
        
#     def delete(self,request,task_id):


#         task=Task.objects.get(id=task_id)
#         task.delete()

#         return Response("Task Deleted Succesfully")



class StudentsMarkList(APIView):

    def post(self,request):

        total=request.data["english_marks"]+request.data["maths_marks"]+request.data["science_marks"]+request.data["tamil_marks"]+request.data["social_marks"]

        average=total/5

        if request.data["english_marks"]>35 and request.data["maths_marks"]>35 and request.data["science_marks"]>35 and request.data["tamil_marks"]>35 and request.data["social_marks"]>35:
            score=True
        else:
            score=False
        
        stu=Students_MarK(english_marks=request.data["english_marks"],maths_marks=request.data["maths_marks"],
        science_marks=request.data["science_marks"],tamil_marks=request.data["tamil_marks"],
        social_marks=request.data["social_marks"],total=total,average=average,score=score)

        stu.save()

        return Response("Student Marks Added")
    def get(self,request,stu_id=None):

        if stu_id==None:
            stu=Students_MarK.objects.all()
            n_stu=Students_mark_Serializer(stu,many=True).data

            return Response(n_stu)
        else:
            stu=Students_MarK.objects.get(id=stu_id)
            n_stu=Students_mark_Serializer(stu).data

            return Response(n_stu)
    
    def put(self,request,stu_id):

        stu=Students_MarK.objects.filter(id=stu_id)

        total=request.data["english_marks"]+request.data["maths_marks"]+request.data["science_marks"]+request.data["tamil_marks"]+request.data["social_marks"]
        average=total/5

        if request.data["english_marks"]>35 and request.data["maths_marks"]>35 and request.data["science_marks"]>35 and request.data["tamil_marks"]>35 and request.data["social_marks"]>35:
            score=True
        else:
            score=False
        
        stu.update(english_marks=request.data["english_marks"],maths_marks=request.data["maths_marks"],
        science_marks=request.data["science_marks"],tamil_marks=request.data["tamil_marks"],
        social_marks=request.data["social_marks"],total=total,average=average,score=score)

        return Response("Student Marks Updated")
    
    def delete(self,request,stu_id):

        stu=Students_MarK.objects.get(id=stu_id)

        stu.delete()

        return Response("Students MarksDeleted Successfully")
    
@api_view(["GET","POST"])
def task_api(request):

    if request.method=="GET":
        task=Task.objects.all()

        n_task=Task_Serializer(task,many=True).data

        return Response(n_task)
    
    if request.method=="POST":

        task=Task_Serializer(data=request.data)

        if task.is_valid():
            task.save()
            return Response("New Task Added")
        else:
            return Response(task.errors)

@api_view(["GET","PUT","DELETE"])
def task_api_byID(request,task_id):

    if request.method=="GET":
        task=Task.objects.get(id=task_id)

        n_task=Task_Serializer(task).data
        
        return Response(n_task)
    
    if request.method=="PUT":
        task=Task.objects.get(id=task_id)

        n_task=Task_Serializer(task,data=request.data,partial=True)

        if n_task.is_valid():
            n_task.save()
            return Response("Task Updated")
        else:
            return Response(n_task.errors)
        
    if request.method=="DELETE":

        task=Task.objects.get(id=task_id)

        task.delete()

        return Response("Task Deleted Successfully")

        
