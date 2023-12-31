from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from .models import Department
from .forms import CreateDepartmentForm


class AddDeparment(LoginRequiredMixin,CreateView):
    model = Department
    form_class = CreateDepartmentForm
    template_name = 'department/add.html'
    success_url= reverse_lazy('department:department_all')
       
    
class UpdateDeparment(LoginRequiredMixin,UpdateView):
    model = Department
    context_object_name='dept'
    form_class = CreateDepartmentForm
    template_name = 'department/update.html'
    success_url= reverse_lazy('department:department_all') 
     
    
class AllDeparment(LoginRequiredMixin,ListView):
    model = Department
    context_object_name='department'
    template_name = 'department/all.html'   
    
class ViewDeparment(LoginRequiredMixin,DetailView):
    model = Department
    context_object_name='dept'
    template_name = 'department/view.html'
    
    
class DeleteDeparment(LoginRequiredMixin,DeleteView):
    model = Department
    context_object_name='dept'  
    # template_name = 'department/confirm_delete.html' 
    success_url= reverse_lazy('department:department_all')           
    