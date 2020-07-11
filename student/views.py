from uuid import uuid4
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from school.common_models import ClassName
from school.forms import RegistrationForm, AddressForm, AttendenceForm
from school.models import CustomUser, USER_TYPE_CHOICE
from student.forms import ParentForm, StudentForm, StudentAttendanceForm
from student.models import Student, StudentAttendance


class StudentAttendance(CreateView):
    form_class = StudentAttendanceForm
    model = StudentAttendance
    template_name = 'school/attendance.html'
    success_url = 'school:attendance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)

        #student = Student.objects.filter(class_name = self.)
        context['attendance_form'] = AttendenceForm()

        return context

    def form_valid(self, form):
        attendance_form = AttendenceForm(self.request.POST)

        if form.is_valid() and attendance_form.is_valid():
            form.save()

class StudentHome(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'student/student_home.html')


class StudentListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if kwargs.get('id'):
            try:
                student = Student.objects.filter(id=kwargs.get('id')).first()
                return render(request, 'school/student_detail.html', {'student': student})
            except Exception as e:
                return HttpResponse('<h1>Student Not Found{{e.message}}</h1>')

        else:
            students = Student.objects.filter(personal_details__is_user_deleted= False)
            return render(request, 'school/student_list.html', {'students': students})


class StudentUpdateView(UpdateView):
    model = CustomUser
    template_name = 'school/student_create_form.html'
    form_class = RegistrationForm
    query_pk_and_slug = 'roll_no'
    pk_url_kwarg = 'roll_no'

    def get_object(self, queryset=None):
        custom_user = self.model.objects.filter(student__roll_no = self.kwargs.get('roll_no')).first()
        return custom_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_form'] = AddressForm(instance= self.object.address_set.all().first())
        context['student_form'] = StudentForm(instance= self.object.student)
        context['parent_form'] = ParentForm(instance= self.object.student.parent_details)
        return context


    def get_success_url(self):
        # return reverse('student:student_detail', kwargs='self.object.id')
        return reverse('student:student_list')


class StudentDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('student:student_list')

    def delete(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.filter(pk=kwargs.get('pk')).first()
            user.is_user_deleted = True
            user.save()

            return HttpResponseRedirect(self.success_url)
        except:
            return HttpResponse('<h1>Student Not Found</h1>')


class StudentCreateView(CreateView):
    model = CustomUser
    template_name = 'school/student_create_form.html'
    form_class = RegistrationForm

    # success_url = reverse_lazy('student:student_create')

    def get_success_url(self):
        return reverse('student:student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_form'] = AddressForm()
        context['student_form'] = StudentForm()
        context['parent_form'] = ParentForm()

        return context

    def is_valid(self, form):
        return form.is_valid()

    def form_valid(self, form):
        address_form = AddressForm(self.request.POST)
        student_form = StudentForm(self.request.POST, self.request.FILES)
        parent_form = ParentForm(self.request.POST)

        if all([self.is_valid(f) for f in [address_form, student_form, parent_form, form]]):
            form.instance.password = str(uuid4())
            form.instance.type_of_user = USER_TYPE_CHOICE[0][0]

            form.save()
            parent_form.save()
            address_form.instance.user = form.instance
            address_form.save()

            student_form.instance.parent_details = parent_form.instance
            student_form.instance.personal_details = form.instance

            student_form.save()

            return super().form_valid(form)
        else:
            return render(self.request, template_name= self.template_name,
                          context= {'address_form': address_form, 'parent_form': parent_form,
                                    'student_form': student_form, 'form':form})

    # handle invalid scenarios form.errors

    # # Validate forms
    # def form_valid(self, form):
    #     ctx = self.get_context_data()
    #     inlines = ctx['inlines']
    #     if inlines.is_valid() and form.is_valid():
    #         self.object = form.save()  # saves Father and Children
    #         return redirect(self.get_success_url())
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))
    #
    # def form_invalid(self, form):
    #     return self.render_to_response(self.get_context_data(form=form))
    #
    # # We populate the context with the forms. Here I'm sending
    # # the inline forms in `inlines`
    # def get_context_data(self, **kwargs):
    #     ctx = super(StudentDetailInfo, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         ctx['form'] = StudentForm(self.request.POST)
    #         ctx['inlines'] = StudentInlineFormSet(self.request.POST)
    #     else:
    #         ctx['form'] = StudentForm()
    #         ctx['inlines'] = StudentInlineFormSet()
    #     return ctx
