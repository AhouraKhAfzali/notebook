"""
# DRF imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# other imports
from api.permissions import AdminOrTeacherPermission
from .models import Course, Enrollment
from .serializers import ClassSerializer, EnrollmentSerializer, EnrollmentSerializerCombined


# Class Model APIs
class ClassCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


class ClassList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]


class ClassFilter(APIView):
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        query_dict = {key: value for key, value in request.data.items() if value}
        try:
            queryset = Course.objects.filter(**query_dict)
            serializer = ClassSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "خطایی رخ داده است، شاید داده نا معتبری وارد شده است."}, status=status.HTTP_400_BAD_REQUEST)


class ClassDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]


class ClassUpdate(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


class ClassDelete(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, AdminOrTeacherPermission]


# EnrollmentRequest Model APIs
class EnrollmentCreate(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]


class EnrollmentList(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializerCombined
    permission_classes = [IsAuthenticated]


class EnrollmentFilter(APIView):
    serializer_class = EnrollmentSerializerCombined
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        query_dict = {key: value for key, value in request.data.items() if value}
        try:
            queryset = Enrollment.objects.filter(**query_dict)
            serializer = EnrollmentSerializerCombined(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            print("it is happening")
            return Response({"detail": "خطایی رخ داده است، شاید داده نا معتبری وارد شده است."}, status=status.HTTP_400_BAD_REQUEST)


class EnrollmentDetail(generics.RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializerCombined
    permission_classes = [IsAuthenticated]


class EnrollmentUpdate(generics.UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]


class EnrollmentDelete(generics.DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
"""