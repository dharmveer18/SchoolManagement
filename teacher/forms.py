from django import forms

from teacher.models import Teacher, Salary


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