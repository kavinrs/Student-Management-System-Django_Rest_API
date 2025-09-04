from django.urls import path, include
from .router import router
from .views import *

urlpatterns = [
    path("rout/",include(router.urls)),
    path("laptop/",LaptopList.as_view()),
    path("laptop/<int:pk>/",LaptopList2.as_view())
]