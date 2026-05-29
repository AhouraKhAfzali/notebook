"""
from rest_framework import serializers
from domains.learning.serializers import ClassSerializer
from accounts.serializers import UserSerializer
from .models import Assignment, Submission

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentSerializerCombined(serializers.ModelSerializer):
    class_obj = ClassSerializer(many=False)
    created_by = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Assignment
        fields = '__all__'

class SubmissionSerializerCombined(serializers.ModelSerializer):
    student = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Submission
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
"""