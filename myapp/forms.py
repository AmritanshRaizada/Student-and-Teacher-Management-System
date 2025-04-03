from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student, Teacher

# Register Form
class RegisterForm(UserCreationForm):
    

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
        exclude = ['created_at']

# Teacher Form
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'email']
