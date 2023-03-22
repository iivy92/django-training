from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListStudentRegistrationsSerializer, ListCourseRegistrationsSerializer

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


class ListStudentRegistrations(generics.ListAPIView):
    """ Lista todas as matriculas de um aluno """
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStudentRegistrationsSerializer


class ListCourseRegistrations(generics.ListAPIView):
    """ Lista todos os alunos matriculados num curso """
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListCourseRegistrationsSerializer
