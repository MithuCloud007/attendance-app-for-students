from django import forms
from attendance.models import Class
    
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        widgets = {
            'class_id': forms.TextInput(attrs={'class': 'form-control '}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'})
        }  