from django import forms

from school.common_models import Address
from school.models import CustomUser


# class RegistrationForm(UserCreationForm):
#     dob = forms.DateField(widget=forms.SelectDateWidget())
#     class Meta:
#         model = CustomUser
#         fields = [ 'first_name', 'last_name', 'username', 'password1', 'password2',
#                    'dob','email', 'mobile_no', 'photo', 'type_of_user'
#
#         ]

class RegistrationForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name', 'username',
                   'dob','email', 'mobile_no', 'photo', ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user',]