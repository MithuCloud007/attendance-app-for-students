from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from attendance.models import Class
from .forms import ClassForm

class AddClass(LoginRequiredMixin,CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'class_app/add.html'
    success_url= reverse_lazy('class_app:class_all')
       
    
class UpdateClass(LoginRequiredMixin,UpdateView):
    model = Class
    context_object_name='classes'
    form_class = ClassForm
    template_name = 'class_app/update.html'
    success_url= reverse_lazy('class_app:class_all') 
     
    
class AllClass(LoginRequiredMixin,ListView):
    model = Class
    context_object_name='classes'
    template_name = 'class_app/all.html'   
    
class ViewClass(LoginRequiredMixin,DetailView):
    model = Class
    context_object_name='classes'
    template_name = 'class_app/view.html'
    
    
class DeleteClass(LoginRequiredMixin,DeleteView):
    model = Class
    context_object_name='classes'  
    template_name = 'class_app/class_confirm_delete.html' 
    success_url= reverse_lazy('class_app:class_all') 
