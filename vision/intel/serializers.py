from rest_framework import serializers
from intel.models import PersonInfo, Image
from django.contrib.auth.models import User


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = "__all__"



class ImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = Image
            fields = "__all__"
      

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()