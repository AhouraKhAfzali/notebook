"""
from rest_framework import serializers
from .models import Grade, Institution, Subject, Specialization, Lesson

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class MajorSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(many=False)
    specializations = SpecializationSerializer(many=True)
    class Meta:
        model = Subject
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    majors = MajorSerializer(many=True)
    class Meta:
        model = Institution
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    majors = MajorSerializer(many=True)
    class Meta:
        model = Lesson
        fields = '__all__'
"""