from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return self.fullname


class Mentor(models.Model):
    fullname = models.CharField(max_length=20)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.fullname


class Course(models.Model):
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name