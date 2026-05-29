"""
from rest_framework import serializers
from domains.academia.serializers import UniversitySerializer, MajorSerializer, SpecializationSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(many=False)
    major = MajorSerializer(many=False)
    specialization = SpecializationSerializer(many=False)
    class Meta:
        model = User
        fields = '__all__'
"""