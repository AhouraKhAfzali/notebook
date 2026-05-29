"""
from rest_framework import serializers
from domains.academia.serializers import UniversitySerializer, MajorSerializer, LessonSerializer
from accounts.serializers import UserSerializer
from .models import Course, Enrollment

class ClassSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(many=False)
    major = MajorSerializer(many=False)
    lesson = LessonSerializer(many=False)
    teacher = UserSerializer(many=False)
    students = UserSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentSerializerCombined(serializers.ModelSerializer):
    student = UserSerializer(many=False)
    class Meta:
        model = Enrollment
        fields = '__all__'
"""