from django.urls import path

from teacher.views import TeacherHome, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, \
    TeacherDeleteView, TeacherAttendanceView

urlpatterns = [
    path('teacher/', TeacherHome.as_view(), name='teacher_home'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/list/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/attendance/', TeacherAttendanceView.as_view(), name='teacher_attendance'),
    path('teacher/<str:emp_id>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/<str:emp_id>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/<str:emp_id>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

]
