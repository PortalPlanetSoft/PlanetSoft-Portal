from django import forms
from .models import Employee

class AddEmployee(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'email', 'position')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'})

        }