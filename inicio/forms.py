from django import forms

class HuespedFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    edad=forms.CharField(max_length=3)
    nacionalidad=forms.CharField(max_length=20)
    