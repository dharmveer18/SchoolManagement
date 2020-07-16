from datetime import datetime

from django.db import models

from school.models import CustomUser


LEAVE_REASON = (
    ('N', 'None'),
    ('S', 'Sick Leave'),
)
ATTENDANCE_STATUS = (
    ('P', 'present'),
    ('A', 'absent'),
    ('L', 'leave'),
    ('H', 'Half-day')
)


class Address(models.Model):
    street = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=30)

    pin_code = models.PositiveIntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class ClassName(models.Model):
    class_name = models.CharField(max_length=20)
    tution_fee = models.FloatField(null=True, blank=True)
    registration_fee = models.FloatField(null=True, blank=True)
    development_fee = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.class_name

class Leaves(models.Model):
    cosumed_leaves = models.PositiveIntegerField()
    allocated_leaves = models.PositiveIntegerField()


class Attendance(models.Model):
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS, default='A')
    reason = models.CharField(max_length=1, choices=LEAVE_REASON)


