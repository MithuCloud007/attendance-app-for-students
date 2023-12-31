from django.contrib import admin
from .models import Class,Student,Attendance,Mentor
# Register your models here.
admin.site.register(Class),
admin.site.register(Student),
admin.site.register(Attendance),
admin.site.register(Mentor)