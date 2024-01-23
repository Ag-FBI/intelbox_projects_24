from rest_framework import serializers
from intel.models import PersonInfo


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = "__all__"
