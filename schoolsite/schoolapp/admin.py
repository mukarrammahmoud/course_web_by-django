from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Login)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Instructor)
