from rest_framework.serializers import ModelSerializer
from .models import Links

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Links
        fields = ["short_link", "full_link"]
        