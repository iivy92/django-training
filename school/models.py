from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=64)
    document_number = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Basis'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, default='B')

    def __str__(self):
        return self.name

class Registration(models.Model):
    SHIFT = (
        ('M', 'Morning'),
        ('E', 'Evening'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    shift = models.CharField(max_length=1, choices=SHIFT, blank=False, default='B')
