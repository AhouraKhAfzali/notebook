"""
# DRF imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# other imports
from api.permissions import AdminOrTeacherPermission
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, AssignmentSerializerCombined, SubmissionSerializer, SubmissionSerializerCombined



# Assignment Model APIs
class AssignmentCreate(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


class AssignmentList(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializerCombined
    permission_classes = [IsAuthenticated]


class AssignmentFilter(APIView):
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        query_dict = {key: value for key, value in request.data.items() if value}
        try:
            queryset = Assignment.objects.filter(**query_dict)
            serializer = AssignmentSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "خطایی رخ داده است، شاید داده نا معتبری وارد شده است."}, status=status.HTTP_400_BAD_REQUEST)


class AssignmentDetail(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializerCombined
    permission_classes = [IsAuthenticated]


class AssignmentUpdate(generics.UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


class AssignmentDelete(generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]

# Submission Model APIs
class SubmissionCreate(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


class SubmissionList(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializerCombined
    permission_classes = [IsAuthenticated]


class SubmissionFilter(APIView):
    serializer_class = SubmissionSerializerCombined
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        query_dict = {key: value for key, value in request.data.items() if value not in ['', None]}
        print(query_dict)
        try:
            queryset = Submission.objects.filter(**query_dict)
            serializer = SubmissionSerializerCombined(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "خطایی رخ داده است، شاید داده نا معتبری وارد شده است."}, status=status.HTTP_400_BAD_REQUEST)


class SubmissionDetail(generics.RetrieveAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializerCombined
    permission_classes = [IsAuthenticated]


class SubmissionUpdate(generics.UpdateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


class SubmissionDelete(generics.DestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]
"""