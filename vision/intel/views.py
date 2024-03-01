from rest_framework.response import Response
from .serializers import PersonInfoSerializer, LoginSerializer, ImageSerializer
from .models import PersonInfo, Image
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout 
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser

class UserView(ListCreateAPIView):
      queryset = PersonInfo()
      serializer_class = PersonInfoSerializer

      def post(self, request,*args, **kwargs):
            serializer = PersonInfoSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      def get(self, request, *args, **kwargs):
            info = PersonInfo.objects.all()
            serializer = PersonInfoSerializer(info, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class ImageView(APIView):
      queryset = Image()
      parser_classes = (MultiPartParser, FormParser)
      def post(self, request,*args, **kwargs):
            serializer = ImageSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      def get(self, request, *args, **kwargs):
            info = self.queryset
            serializer = ImageSerializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
      def post(self, request, *args, **kwargs):
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                  username = serializer.validated_data["username"]
                  password = serializer.validated_data["password"]
                  user = authenticate(request,username=username, password=password)

                  if user is not None:
                        login(request, user)
                        return Response({"message":"successful"}, status=status.HTTP_200_OK)
                  else:
                        return Response({"Error":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
      def post(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                  logout(request)
            return Response({"Response":"Logged_out"}, status=status.HTTP_200_OK)     