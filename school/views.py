from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListStudentRegistrationsSerializer, ListCourseRegistrationsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """ Exibir todos os alunos """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['document_number', 'name']


class CoursesViewSet(viewsets.ModelViewSet):
    """ Exibir todos os cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', ] 


class RegistrationsViewSet(viewsets.ModelViewSet):
    """ Exibir todos as matriculas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListStudentRegistrations(generics.ListAPIView):
    """ Lista todas as matriculas de um aluno """
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStudentRegistrationsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListCourseRegistrations(generics.ListAPIView):
    """ Lista todos os alunos matriculados num curso """
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListCourseRegistrationsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
