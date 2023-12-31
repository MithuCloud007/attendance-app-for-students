from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from attendance.models import Student
from .forms import StudentForm


class AddStudentView(LoginRequiredMixin,CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/add.html'
    success_url= reverse_lazy('student:student_all')
       
    
class UpdateStudentView(LoginRequiredMixin,UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/update.html'
    success_url= reverse_lazy('student:student_all') 
     
    
class AllStudentView(LoginRequiredMixin,ListView):
    model = Student
    context_object_name='student'
    template_name = 'student/all.html'   
    
class ViewStudent(LoginRequiredMixin,DetailView):
    model = Student
    context_object_name='student'
    template_name = 'student/view.html'
    
    
class DeleteStudent(LoginRequiredMixin,DeleteView):
    model = Student
    context_object_name='student'   
    template_name = 'student/student_confirm_delete.html'
    
    success_url= reverse_lazy('student:student_all')  
