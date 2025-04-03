from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Teacher
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)


admin.site.register(Student)
admin.site.register(Teacher)


