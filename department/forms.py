from django import forms
from .models import Department

class CreateDepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=250,help_text = "Course Name Field is required.")
    description = forms.Textarea()

    class Meta:
        model= Department
        fields = ('name','description','status')