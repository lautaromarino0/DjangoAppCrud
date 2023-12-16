from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tittle', 'description', 'important']
        widgets = {
            'tittle' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese un titulo'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Ingrese una descripcion'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-input m-auto'})
        }