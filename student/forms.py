from django import forms
from attendance.models import Student
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = {
            'class_id',
            'department_name',
            'mentor_name'
        }
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control '}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'department_name': forms.Select(attrs={'class': 'form-control'}),
            'mentor_name': forms.Select(attrs={'class': 'form-control'}),
     
        }  