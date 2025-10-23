# antiguedades/forms.py
from django import forms
from .models import Antiguedad

class AntiguedadForm(forms.ModelForm):
    class Meta:
        model = Antiguedad
        # Campos que se mostrarán en los formularios de Crear y Editar
        fields = ['nombre_pieza', 'precio']
        
        # Etiquetas personalizadas para el HTML
        labels = {
            'nombre_pieza': 'Nombre de la Pieza',
            'precio': 'Precio',
        }
        
        # Widgets para aplicar estilos de Bootstrap 'form-control' [01:16:17]
        widgets = {
            'nombre_pieza': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }