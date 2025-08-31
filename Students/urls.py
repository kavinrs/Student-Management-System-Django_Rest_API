from django.urls import path
from .views import StudentList,TaskList,TaskList_By_ID

urlpatterns = [
    path('student/',StudentList.as_view()),
    path("student/<int:student_id>/",StudentList.as_view()),
    path("task/",TaskList.as_view()),
    path("task/<int:task_id>/",TaskList_By_ID.as_view())
]