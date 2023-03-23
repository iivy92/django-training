from rest_framework import serializers
from school.models import Student, Course, Registration
from school.validators import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'document_number', 'birth_date')
    
    def validate(self, data):
        if not valid_document_number(data['document_number']):
            raise serializers.ValidationError({'document_number': "Document Number must be 11 characters"})

        if not valid_name(data['name']):
            raise serializers.ValidationError({'name': "Name must contain only alphabetic characters"})
        
        return data
    

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
