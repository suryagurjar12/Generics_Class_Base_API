from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics


class Stu_list(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Stu_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
