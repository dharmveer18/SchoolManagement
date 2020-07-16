from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseFormSet


from school.common_models import ATTENDANCE_STATUS, Attendance, LEAVE_REASON
from student.models import Parent, Student, StudentAttendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'class_name']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'contact_no']


class StudentAttendanceForm(forms.Form):
    student_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    roll_no = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    attendance = forms.ChoiceField(choices=ATTENDANCE_STATUS)  # add choices
    reason = forms.ChoiceField(choices=LEAVE_REASON, validators=[])  # add class hidden
    class_name = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, class_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_name = class_name

        self.fields['class_name'].initial = self.class_name.id

    def clean(self):
        super().clean()
        clean_data = self.cleaned_data

        if clean_data['attendance'] in ('A', 'L', 'H'):
            if clean_data['reason'] == 'N':
                raise ValidationError('Please provide reason')

    def save(self):
        clean_data = self.cleaned_data
        roll_no = clean_data['roll_no']
        status = clean_data['attendance']
        reason = clean_data['reason']

        attendance = Attendance.objects.get_or_create(status=status, reason=reason)
        attendance = Attendance.objects.get(status=status, reason=reason)
        student = Student.objects.filter(roll_no=roll_no).first()

        student_attendance = StudentAttendance.objects.create(attendance=attendance, student=student,
                                                              date=str(self.data['student_attend_date']),
                                                              class_name=self.class_name)

        return student_attendance


class StudentAttendanceBaseFormSet(BaseFormSet):

    def clean(self):
        super().clean()
        if self.data['student_attend_date'] > str(date.today()):
            raise ValidationError( 'Date  shouldnot be greater than today' )


