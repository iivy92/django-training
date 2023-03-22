from rest_framework import viewsets
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """ Exibir todos os alunos """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """ Exibir todos os cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    """ Exibir todos as matriculas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
