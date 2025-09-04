from django.urls import path, include
from .router import router
from .views import *

urlpatterns = [
    path("rout/",include(router.urls)),
    path("laptop/",BookList.as_view()),
    path("laptop/<int:pk>/",BookList2.as_view())
]