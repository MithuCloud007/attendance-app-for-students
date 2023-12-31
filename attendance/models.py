from django.db import models
from department.models import Department

class Class(models.Model):
    class_id = models.CharField(max_length=255,default = 'c00x')
    class_name = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name
       
class Mentor(models.Model):
    mentor_name = models.CharField(max_length=250)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='mentor_classId')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mentor_name
           
class Student(models.Model):
    student_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='student_departmentName')
    mentor_name = models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name='student_mentorName')
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='student_classId')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id  
    
class Attendance(models.Model):
    STATUS_OPTIONS = (('present','present'),('absent','absent'))
    status = models.CharField(max_length=255,choices=STATUS_OPTIONS,default='absent')
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendance_studentId')
    # department_name = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='attendance_departmentName')
    # mentor_name = models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name='attendance_mentorName')
    # class_id = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='attendance_classId')
    attendance_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"{self.student_id.first_name}"