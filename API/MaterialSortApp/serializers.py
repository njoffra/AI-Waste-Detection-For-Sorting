from rest_framework import serializers
from .models import RecognitionResult


class RecognitionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognitionResult
        fields = '__all__'
        