from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate
from .serializers import *

class UserAPI(APIView):

    def post(self,request):

        new_user=User(username=request.data["username"],is_superuser=request.data["is_superuser"])

        new_user.set_password(request.data["password"])

        new_user.save()

        return Response("New user Added")

class Authenticate_User(APIView):

    def post(self,request):

        # user=authenticate(username=request.data["username"],password=request.data["password"])

        # if user==None:
        #     return Response("Username or Password is invalid . Try Again")
        # else:
        #     return Response("User is valid")

        usr=Auth_Serializers(data=request.data)

        if usr.is_valid():
            return Response(usr.validated_data)
        else:
            return Response(usr.errors)