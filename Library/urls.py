from django.urls import path, include
from .router import router

urlpatterns = [
    path("rout/",include(router.urls)),
]