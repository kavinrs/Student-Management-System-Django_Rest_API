from django.urls import path
from .views import *

urlpatterns = [
    path('student/',StudentList.as_view()),
    path("student/<int:student_id>/",StudentList.as_view()),
    path("task/",TaskList.as_view()),
    path("task/<int:task_id>/",TaskList.as_view()),
    path("studentmark/",StudentsMarkList.as_view()),
    path("studentmark/<int:stu_id>/",StudentsMarkList.as_view()),
    path("taskfunc/",task_api),
    path("taskfunc/byid/<int:task_id>/",task_api_byID)
]