from django.urls import path
from student.views import AddStudentView,AllStudentView,UpdateStudentView,DeleteStudent,ViewStudent
app_name='student'

urlpatterns = [
    path('student-add', AddStudentView.as_view(), name="student_add"),
    path('student-all', AllStudentView.as_view(), name="student_all"),
    path('student-detail/<int:pk>', ViewStudent.as_view(), name="student_view"),
    path('student-update/<int:pk>', UpdateStudentView.as_view(), name="student_update"),
    path('student-delete/<int:pk>', DeleteStudent.as_view(), name="student_delete")
]