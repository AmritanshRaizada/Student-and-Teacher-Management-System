"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import (
    home, student_list, student_detail, student_create, 
    student_update, student_delete, teacher_detail, teacher_create,user_login,user_logout,
    register,login_view,logout_view
)
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', login_view, name='login'),
    path('login/', user_login, name='login'),
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('student/<int:id>/', student_detail, name='student_detail'),
    path('student/create/', student_create, name='student_create'),
    path('student/update/<int:id>/', student_update, name='student_update'),
    path('student/delete/<int:id>/', student_delete, name='student_delete'),

    path('teacher/<int:id>/', teacher_detail, name='teacher_detail'),
    path('teacher/create/', teacher_create, name='teacher_create'),
]

