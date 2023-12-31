from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView
from django.urls import reverse_lazy
from .models import Attendance
from .forms import CreateAttendance


class AttendanceListCreateView(LoginRequiredMixin,CreateView,ListView):
    model = Attendance
    form_class = CreateAttendance
    context_object_name='attendance'
    template_name = 'attendance/add-list.html'  
    success_url= reverse_lazy('attendance:attendance_all')    
  
class ViewAttendance(LoginRequiredMixin,DetailView):
    model = Attendance
    context_object_name='att'
    template_name = 'attendance/view.html'   

 