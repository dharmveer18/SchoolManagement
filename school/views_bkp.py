from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import login
from django.urls import reverse
from django.views.generic.base import View

from django.views.generic.edit import CreateView

class CustomLogout(LogoutView):
    form_class =
# class LoginView(FormView):
#     """
#     This is a class based version of django.contrib.auth.views.login.
#     Usage:
#         in urls.py:
#             url(r'^login/$',
#                 AuthenticationView.as_view(
#                     form_class=MyCustomAuthFormClass,
#                     success_url='/my/custom/success/url/),
#                 name="login"),
#     """
#     form_class = AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#     template_name = 'registration/login.html'
#
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, *args, **kwargs):
#         return super(LoginView, self).dispatch(*args, **kwargs)
#
#     def form_valid(self, form):
#         """
#         The user has provided valid credentials (this was checked in AuthenticationForm.is_valid()). So now we
#         can log him in.
#         """
#         login(self.request, form.get_user())
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         if self.success_url:
#             redirect_to = self.success_url
#         else:
#             redirect_to = self.request.GET.get(self.redirect_field_name, '')
#
#         #netloc = urlparse.urlparse(redirect_to)[1]
#         if not redirect_to:
#             redirect_to = settings.LOGIN_REDIRECT_URL
#         # Security check -- don't allow redirection to a different host.
#         #elif netloc and netloc != self.request.get_host():
#             #redirect_to = settings.LOGIN_REDIRECT_URL
#         return redirect_to
#
#     def set_test_cookie(self):
#         self.request.session.set_test_cookie()
#
#     def check_and_delete_test_cookie(self):
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#             return True
#         return False
#
#     def get(self, request, *args, **kwargs):
#         """
#         Same as django.views.generic.edit.ProcessFormView.get(), but adds test cookie stuff
#         """
#         self.set_test_cookie()
#         return super(LoginView, self).get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Same as django.views.generic.edit.ProcessFormView.post(), but adds test cookie stuff
#         """
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         if form.is_valid():
#             self.check_and_delete_test_cookie()
#             return self.form_valid(form)
#         else:
#             self.set_test_cookie()
#             return self.form_invalid(form)
from school.forms import RegistrationForm
from school.models import CustomUser


class RegisterUser(CreateView):
    form_class = RegistrationForm
    model = CustomUser
    template_name = 'registration/registration.html'

    success_url = 'school:register'


class PhaseOneLoginView(LoginView):
    def form_valid(self, form):
        """
        Forces superusers to login in a 2 step process (One Time Password). Other users are logged in normally
        """
        user = form.get_user()
        if user.type_of_user == 's':
            print('student')
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            print('admin')
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())

    def get_phase_two_url(self):
        return reverse('school:')

    def save_user(self, user):
        self.request.session['otp_user'] = user


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'school/home.html')

# from django.utils.http import is_safe_url, url_has_allowed_host_and_scheme
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic import FormView, RedirectView, TemplateView
# from django.views.generic.base import View
#
#
# class LoginView(FormView, TemplateView):
#     """
#     Provides the ability to login as a user with a username and password
#     """
#     template_name="school/login.html"
#
#     success_url = 'school:home'
#
#     form_class = AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#
#     @method_decorator(sensitive_post_parameters('password'))
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         # Sets a test cookie to make sure the user has cookies enabled
#         request.session.set_test_cookie()
#
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         auth_login(self.request, form.get_user())
#
#         # If the test cookie worked, go ahead and
#         # delete it since its no longer needed
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#
#         return super(LoginView, self).form_valid(form)
#
#     def get_success_url(self):
#         redirect_to = self.request.GET.get(self.redirect_field_name)
#         if not is_safe_url(url=redirect_to, host =self.request.get_host(), require_https=True):
#         #if not url_has_allowed_host_and_scheme(url=redirect_to, host=self.request.get_host()):
#             redirect_to = self.success_url
#         return redirect_to
#
#
# def auth_logout(request):
#     pass
#
#
# class LogoutView(RedirectView):
#     """
#     Provides users the ability to logout
#     """
#     url = '/auth/login/'
#
#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)
#
