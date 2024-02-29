from rest_framework import serializers
from intel.models import PersonInfo, Image


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Image
        fields = "__all__"
    
      




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()