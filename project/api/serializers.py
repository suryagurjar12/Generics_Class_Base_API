from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    method=Student
    field=["id","name","email","city","contact"]