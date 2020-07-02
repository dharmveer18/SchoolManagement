from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from school.models import CustomUser
from student.models import Parent, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'class_name']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'contact_no']





# ParentInlineFormSet = inlineformset_factory(
#     Parent, Address,
#     form= AddressForm
# )
#
# StudentInlineFormSet = inlineformset_factory(
#     Student, Parent,
#     form = ParentInlineFormSet
# )