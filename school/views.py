from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from school.forms import RegistrationForm
from school.models import CustomUser


class RegisterUser(CreateView):
    form_class = RegistrationForm
    model = CustomUser
    template_name = 'registration/registration.html'

    success_url = reverse_lazy('school:register')

class CustomLoginView(LoginView):
    def home(self):
        user = self.request.user
        if user.type_of_user == 't':
            return HttpResponseRedirect(reverse('teacher:teacher_home'))
        elif user.type_of_user == 's':
            return HttpResponseRedirect(reverse('student:student_home'))
        else :
            return HttpResponseRedirect(reverse('school:admin_home'))

    def form_valid(self, form):
        user = form.get_user()
        if not user.password:
            forms.ValidationError('Password cannot be Null')
        login(self.request, user)

        return self.home()

    def save_user(self, user):
        self.request.session['otp_user'] = user

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.home()
        else:
            return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.home()
        else:
            return super().post(self, request, *args, **kwargs)


class AdminHome(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'school/admin_home.html')








