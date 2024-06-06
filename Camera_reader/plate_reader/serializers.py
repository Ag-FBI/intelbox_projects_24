from rest_framework.serializers import ModelSerializer
from.models import Info

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

