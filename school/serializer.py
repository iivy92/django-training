from rest_framework import serializers
from school.models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'document_number', 'birth_date')
    
    def validate_document_number(self, document_number):
        if len(document_number) != 11:
            raise serializers.ValidationError("Document Number must be 11 characters")
        return document_number

    def validate_name(self, name):
        if not name.isalpha():
            raise serializers.ValidationError("Name must contain only alphabetic characters ")

        return name

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class ListStudentRegistrationsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')
    shift = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ('course', 'shift')
    
    def get_shift(self, obj):
        return obj.get_shift_display()


class ListCourseRegistrationsSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ('student_name', )
