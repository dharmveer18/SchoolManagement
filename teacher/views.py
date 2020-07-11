from uuid import uuid4
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from school.forms import RegistrationForm, AddressForm
from school.models import CustomUser, USER_TYPE_CHOICE
from teacher.forms import TeacherForm, SalaryForm
from teacher.models import Teacher


class TeacherHome(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'teacher/teacher_home.html')


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    success_url = 'teacher:teacher_list'

    def get_queryset(self):
        return super().get_queryset().filter(personal_details__is_user_deleted= False)


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'school/customuser_confirm_delete.html'
    success_url = reverse_lazy('teacher:teacher_list')
    query_pk_and_slug = 'emp_id'
    pk_url_kwarg = 'emp_id'

    # slug_url_kwarg = 'emp_id'

    def get_object(self, queryset=None):
        teacher_instance = self.model.objects.filter(teacher__emp_id=self.kwargs.get('emp_id')).first()
        return teacher_instance

    def delete(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            user.is_user_deleted = True
            user.save()
            # delete database with related items
            return HttpResponseRedirect(self.success_url)
        except:
            return HttpResponse('<h1>Teacher Not Found</h1>')


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'teacher/teacher_create_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('teacher:teacher_list')
    query_pk_and_slug = 'emp_id'
    pk_url_kwarg = 'emp_id'

    def get_object(self, queryset=None):
        teacher_instance = self.model.objects.filter(teacher__emp_id=self.kwargs.get('emp_id')).first()
        return teacher_instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_form'] = AddressForm(instance=self.object.address_set.all().first())

        context['teacher_form'] = TeacherForm(instance=self.object.teacher)
        context['salary_form'] = SalaryForm(instance=self.object.teacher.salary)

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_form = AddressForm(self.request.POST, instance=self.object.address_set.all().first())
        salary_form = SalaryForm(self.request.POST, instance=self.object.teacher.salary)
        teacher_form = TeacherForm(self.request.POST, self.request.FILES, instance=self.object.teacher)

        if form.is_valid() and address_form.is_valid() and teacher_form.is_valid():

            form.save()
            address_form.save()
            teacher_form.save()
            salary_form.save()

            return super().form_valid(form)
        else:
            return render(self.request, template_name=self.template_name,
                          context={'address_form': address_form, 'teacher_form': teacher_form, 'form': form})


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'teacher/teacher_detail.html'
    success_url = 'teacher:teacher_detail'
    query_pk_and_slug = 'emp_id'
    pk_url_kwarg = 'emp_id'

    def get_object(self, queryset=None):
        teacher_detail = self.model.objects.filter(teacher__emp_id=self.kwargs.get('emp_id')).first()
        return teacher_detail


class TeacherCreateView(CreateView):
    model = CustomUser
    template_name = 'teacher/teacher_create_form.html'
    form_class = RegistrationForm
    success_url = 'teacher:teacher_create'

    def get_success_url(self):
        return reverse('teacher:teacher_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_form'] = AddressForm()
        context['teacher_form'] = TeacherForm()
        context['salary_form'] = SalaryForm()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_form = AddressForm(self.request.POST)
        salary_form = SalaryForm(self.request.POST)
        teacher_form = TeacherForm(self.request.POST, self.request.FILES)

        if form.is_valid() and address_form.is_valid() and teacher_form.is_valid():
            form.instance.password = str(uuid4())
            form.instance.type_of_user = USER_TYPE_CHOICE[1][0]

            form.save()
            address_form.instance.user = form.instance
            address_form.save()
            teacher_form.instance.personal_details = form.instance
            teacher_form.save()
            salary_form.instance.teacher_id = teacher_form.instance
            salary_form.save()

            return super().form_valid(form)

        else:
            return render(self.request, template_name=self.template_name,
                          context={'address_form': address_form, 'teacher_form': teacher_form, 'form': form})
