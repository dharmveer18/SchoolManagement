from django.http import HttpResponse
from django.urls import reverse


class CheckPermissions():

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        #Can I avoid more if-else?

        if request.user.is_authenticated:
            if request.path in ('/'):
                return
            if request.user.type_of_user == 'a':
                #reverse_lazy
                if request.path in ('/student/list/',reverse('student:student_create'),reverse('student:student_update', view_kwargs['roll_no'])):
                # 'student/<int:roll_no>/update/'
                # 'student/<pk>/delete/' Need to check
                    pass
            elif request.user.type_of_user == 's':
                if request.path in ('/'):
                    pass
                else:
                    return HttpResponse('<h1>Un-Authorised Access</h1>')
            elif request.user.type_of_user == 't':
                if request.path in ('/'):
                    pass
                else:
                    return HttpResponse('<h1>Un-Authorised Access</h1>')
        elif request.user.is_authenticated == False and request.path == '/login/':
            pass
        else:
            return HttpResponse('<h1>Un-Authorised Access</h1>')


    # def process_request(self, request):
    #
    # def process_template_response(self, request, response):
    #
    # def process_exception(self, request, exception):
    # Customised Exception or HttpErrors by using custom view