from .models import Otter
from rest_framework import serializers


class OtterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otter
        fields = ["id", "name", "sex", "age"]
