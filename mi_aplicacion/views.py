# mi_aplicacion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('lista_tareas')
    return render(request, 'crear_tarea.html')

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.save()
        return redirect('lista_tareas')
    return render(request, 'editar_tarea.html', {'tarea': tarea})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})
