from django.contrib import admin
from school.models import Student, Course


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'document_number', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'document_number')
    list_per_page = 20

admin.site.register(Student, Students)


class Courses(admin.ModelAdmin): 
    list_display = ('id', 'name', 'description', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Course, Courses)
