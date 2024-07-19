from django import forms

class BuscarHuesped(forms.Form):
    nombre=forms.CharField(max_length=20,required=False)