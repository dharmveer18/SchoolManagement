from django.db import models

from school.common_models import ClassName
from school.models import CustomUser


class Parent(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=13)


class Student(models.Model):
    personal_details = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10, unique= True)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    parent_details = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.personal_details.username
