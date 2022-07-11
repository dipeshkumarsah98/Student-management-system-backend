from rest_framework import serializers
from .models import Student, Grade, Section
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class SectionSerializer(serializers.ModelSerializer):
    total_student = serializers.IntegerField(read_only=True)
    class Meta:
        model = Section
        fields = "__all__"


class SimpleSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name']


class GradeSerializer(serializers.ModelSerializer):
    total_student = serializers.IntegerField(read_only=True)

    class Meta:
        model = Grade
        fields = ["id", "name", 'total_student']


class SimpleGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ["id", "name"]


class StudentSerializer(serializers.ModelSerializer):
    Grade = SimpleGradeSerializer()
    Section = SimpleSectionSerializer()

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'address','contact', 'Grade', 'Section']


class SimpleStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username','first_name','last_name', 'is_superuser', 'is_staff']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'is_superuser', 'is_staff']