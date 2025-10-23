from django.shortcuts import render

# Create your views here.
# antiguedades/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Antiguedad
from .forms import AntiguedadForm

# 1. READ (Listar)
def index(request):
    antiguedades_list = Antiguedad.objects.all()
    context = {'antiguedades': antiguedades_list}
    return render(request, 'antiguedades/index.html', context)

# 2. READ (Detalle - Redirecciona, el modal lo maneja el template) [00:58:38]
def view_antiguedad(request, pk):
    # Busca la antigüedad. La función solo redirige de vuelta,
    # pero asegura que el ID es válido antes de que el modal lo muestre
    antiguedad = get_object_or_404(Antiguedad, pk=pk)
    return redirect(reverse('index'))

# 3. CREATE (Añadir) [01:18:23]
def add(request):
    success = False
    if request.method == 'POST':
        form = AntiguedadForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el nuevo objeto en la DB
            success = True
            form = AntiguedadForm() # Muestra un formulario vacío de nuevo
    else:
        form = AntiguedadForm() # Formulario vacío para GET

    context = {'form': form, 'success': success}
    return render(request, 'antiguedades/add.html', context)

# 4. UPDATE (Editar) [01:39:15]
def edit(request, pk):
    success = False
    antiguedad = get_object_or_404(Antiguedad, pk=pk)

    if request.method == 'POST':
        # Formulario ligado a los datos POST Y a la instancia existente
        form = AntiguedadForm(request.POST, instance=antiguedad)
        if form.is_valid():
            form.save() # Actualiza el objeto existente
            success = True
            form = AntiguedadForm(instance=antiguedad) # Recarga el formulario actualizado
    else:
        # Muestra el formulario precargado con los datos de la instancia
        form = AntiguedadForm(instance=antiguedad) 

    context = {'form': form, 'antiguedad': antiguedad, 'success': success}
    return render(request, 'antiguedades/edit.html', context)

# 5. DELETE (Eliminar) [01:47:00]
def delete(request, pk):
    if request.method == 'POST':
        antiguedad = get_object_or_404(Antiguedad, pk=pk)
        antiguedad.delete() # Elimina el objeto de la DB
    return redirect(reverse('index'))