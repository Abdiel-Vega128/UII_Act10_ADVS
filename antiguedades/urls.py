# antiguedades/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # READ: Lista de todas las antigüedades
    path('', views.index, name='index'), 
    # CREATE: Formulario para añadir una nueva antigüedad
    path('add/', views.add, name='add'), 
    # READ (detalle): Para el modal de información. El <int:pk> captura el ID
    path('<int:pk>/', views.view_antiguedad, name='view_antiguedad'), 
    # UPDATE: Formulario para editar una antigüedad existente
    path('edit/<int:pk>/', views.edit, name='edit'), 
    # DELETE: Petición POST para eliminar una antigüedad
    path('delete/<int:pk>/', views.delete, name='delete'), 
]