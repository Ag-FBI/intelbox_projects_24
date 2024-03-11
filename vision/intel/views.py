from rest_framework.response import Response
from .serializers import PersonInfoSerializer, LoginSerializer, ImageSerializer
from .models import PersonInfo, Image
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout 
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from pathlib import Path
import pickle
import numpy as np
import face_recognition, imutils
from datetime import datetime
from collections import Counter
import cv2
import PySimpleGUI as sg
from multiprocessing import Lock, Queue


DEFAULT_ENCODINGS_PATH = Path("../vision/output/encodings.pkl")
def recognize_faces(
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)
        return loaded_encodings




class UserView(CreateAPIView):
      serializer_class = PersonInfoSerializer

      def post(self, request,*args, **kwargs):
            data = PersonInfoSerializer(data = request.data)
            if data.is_valid():
                   return Response(data.data, status=status.HTTP_201_CREATED)  
            return Response(print(data.errors), status=status.HTTP_400_BAD_REQUEST)
      

class ImageView(APIView):
      queryset = Image()
      parser_classes = (MultiPartParser, FormParser)
      def post(self, request,*args, **kwargs):
            if "image" in request.FILES:
                  image = request.FILES["image"]
                  input_image = face_recognition.load_image_file(image)
                  input_face_locations = face_recognition.face_locations(
                  input_image
                   )
                  input_face_encodings = face_recognition.face_encodings(
                  input_image, input_face_locations
                  )
                  for bounding_box, unknown_encoding in zip(
                  input_face_locations, input_face_encodings
                  ):
                        name = _recognize_face(unknown_encoding, recognize_faces())
                        if not name:
                              name = "Unknown"
                        print(name)

            
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



def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]     