from django.db import models

from school.models import CustomUser


class Teacher(models.Model):
    personal_details = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    joining_date = models.DateField()
    emp_id = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.personal_details.username


class Salary(models.Model):
    basic_salary = models.FloatField()
    hra = models.FloatField(null = True, blank=True)
    pf = models.FloatField(null = True, blank=True)
    da = models.FloatField(null = True, blank=True)
    other_allowances = models.FloatField(null = True, blank=True)
    net_salary = models.FloatField()
    teacher_id = models.OneToOneField(Teacher, on_delete=models.CASCADE)


# class Subject(models.Model):
#     subject_name = models.CharField()
#     marks = models.IntegerField()
#     #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     #student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#
# class Result(models.Model):
#     subject_name = models.ForeignKey(Subject)
#     total_marks = models.FloatField()
#     student = models.ForeignKey(Student)
#
#
# class Attendence(models.Model):
#     student = models.ForeignKey(Student)
#     teacher = models.ForeignKey(Teacher)
#     Subject = models.ForeignKey(Subject)
#
#     status = models.BooleanField()
#     remarks = models.CharField(max_length=255)
#
#
# class Syllabus(models.Model):
#     subject = models.ForeignKey(Subject)
#     teacher = models.ForeignKey(Teacher)
#
#     syllabus = models.FileField()
#
#
# class Events(models.Model):
#     type = models.ChoiceField()
#     organiser = models.ForeignKey(Teacher)
#
#     participants = models.ForeignKey(Student)
#     date_of_event = models.DateField()
#
#
# class Leaves(models.Model):
#     student = models.ForeignKey(Student)
#     teacher = models.ForeignKey(Teacher)
#
#     applied_leaves = models.IntegerField()
#     total_leaves = models.IntegerField()
#
#     remarks = models.CharField(max_length=255)
