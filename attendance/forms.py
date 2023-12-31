from django import forms
from .models import Attendance
    
class CreateAttendance(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = {
            'class_id','department_name','mentor_name'
        }
        widgets = {
        
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect(attrs={'class': ' '}),
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'department_name': forms.Select(attrs={'class': 'form-control'}),
            'mentor_name': forms.Select(attrs={'class': 'form-control'}),
     
        }    