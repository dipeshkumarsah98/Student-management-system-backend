from django.db.models.aggregates import Count
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .models import Student, Grade, Section
from .serializer import StudentSerializer, GradeSerializer, SectionSerializer, AdminSerializer, SimpleStudentSerializer
from .permisssion import IsAdminOrReadOnly


class StudentViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return SimpleStudentSerializer
        return StudentSerializer


class GradeViewSet(ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Grade.objects.annotate(total_student=Count('student')).all()
    serializer_class = GradeSerializer


class SectionViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Section.objects.annotate(total_student=Count('student')).all()
    serializer_class = SectionSerializer


class NestedSectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer

    def get_queryset(self):
        return Section.objects.filter(grade_id=self.kwargs['grade_pk']).annotate(total_student=Count('student')).all()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
