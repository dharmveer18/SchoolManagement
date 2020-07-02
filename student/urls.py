"""SchoolMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from student.views import StudentCreateView, StudentHome, StudentDeleteView, StudentListView, StudentUpdateView

urlpatterns = [
    path('student/', StudentHome.as_view(), name='student_home'),
    path('student/list/', StudentListView.as_view(), name='student_list'),
    path('student/<int:id>/', StudentListView.as_view(), name='student_detail'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:roll_no>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
