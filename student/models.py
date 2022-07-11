from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)


class Section(models.Model):
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
