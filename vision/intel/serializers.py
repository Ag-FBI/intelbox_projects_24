from rest_framework import serializers
from intel.models import PersonInfo, Image


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = "__all__"

class ImageSerializer(serializers.Serializer):
        image = serializers.ImageField()
    
      




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()