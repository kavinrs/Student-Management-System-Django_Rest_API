from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path("user/",UserAPI.as_view()),
    path("userauth/",Authenticate_User.as_view()),
    path("token/",TokenObtainPairView.as_view()),
    path("refresh/",TokenRefreshView.as_view())

]