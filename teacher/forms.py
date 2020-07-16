import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms.formsets import BaseFormSet, formset_factory

from school.common_models import ATTENDANCE_STATUS, LEAVE_REASON, Attendance
from teacher.models import Teacher, Salary, TeacherAttendance


class TeacherForm(forms.ModelForm):
    joining_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Teacher
        fields = ['designation', 'emp_id', 'joining_date']


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = [
            'basic_salary',
            'hra',
            'pf',
            'da',
            'other_allowances',
            'net_salary',
        ]


class TeacherAttendanceForm(forms.Form):
    teacher_name = forms.CharField(widget=forms.TextInput())
    emp_id = forms.CharField(widget=forms.TextInput())
    attendance = forms.ChoiceField(choices=ATTENDANCE_STATUS)
    reason = forms.ChoiceField(choices= LEAVE_REASON)

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    def clean(self):
        super().clean()
        clean_data = self.cleaned_data

        if clean_data['attendance'] in ('A', 'L', 'H'):
            if clean_data['reason'] == 'N':
                raise ValidationError('Please provide reason')

    def save(self):

        emp_id = self.cleaned_data['emp_id']
        status = self.cleaned_data['attendance']
        reason = self.cleaned_data['reason']

        attendance = Attendance.objects.get_or_create(status=status, reason= reason)
        attendance = Attendance.objects.get(status=status, reason=reason)

        teacher = Teacher.objects.filter(emp_id=emp_id).first()
        TeacherAttendance.objects.create(attendance=attendance, teacher = teacher, date= str(self.data['teacher_attend_date']))


class TeacherAttendanceBaseFormset(BaseFormSet):

    def clean(self):
        super().clean()
        if self.data['teacher_attend_date'] > str(datetime.date.today()):
            raise ValidationError("Date shouldn't be greater than today")







