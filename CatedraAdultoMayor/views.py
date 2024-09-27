# hogar/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Anciano, ContactoEmergencia, Enfermedad
from django.urls import reverse
from django.db.models import Count

def dashboard(request):
    # Contar el total de ancianos
    total_ancianos = Anciano.objects.count()

    # Contar el total de contactos
    total_contactos = ContactoEmergencia.objects.count()

    # Contar el total de enfermedades únicas
    total_enfermedades_unicas = Enfermedad.objects.values('nombre_enfermedad').distinct().count()

    return render(request, 'dashboard.html', {
        'total_ancianos': total_ancianos,
        'total_contactos': total_contactos,
        'total_enfermedades_unicas': total_enfermedades_unicas,
    })

def lista_contactos_todos(request):
    contactos = ContactoEmergencia.objects.select_related('anciano').all()
    return render(request, 'lista_contactos_todos.html', {'contactos': contactos})

def lista_ancianos(request):
    ancianos = Anciano.objects.all().prefetch_related('enfermedades')  # Incluye las enfermedades
    return render(request, 'lista_ancianos.html', {'ancianos': ancianos})

# Crear anciano
def crear_anciano(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        edad = request.POST.get('edad')
        direccion = request.POST.get('direccion')
        genero = request.POST.get('genero')
        Anciano.objects.create(nombre=nombre, apellidos=apellidos, edad=edad, direccion=direccion, genero=genero)
        return redirect('lista_ancianos')
    return render(request, 'crear_anciano.html')

# Editar anciano
def editar_anciano(request, id):
    anciano = get_object_or_404(Anciano, id=id)
    if request.method == 'POST':
        anciano.nombre = request.POST.get('nombre')
        anciano.apellidos = request.POST.get('apellidos')
        anciano.edad = request.POST.get('edad')
        anciano.direccion = request.POST.get('direccion')
        anciano.genero = request.POST.get('genero')
        anciano.save()
        return redirect('lista_ancianos')
    return render(request, 'editar_anciano.html', {'anciano': anciano})

# Eliminar anciano
def eliminar_anciano(request, id):
    anciano = get_object_or_404(Anciano, id=id)
    if request.method == 'POST':
        anciano.delete()
        return redirect('lista_ancianos')
    return render(request, 'eliminar_anciano.html', {'anciano': anciano})




# Listar contactos de un anciano
def lista_contactos(request, anciano_id):
    anciano = get_object_or_404(Anciano, id=anciano_id)
    contactos = anciano.contactos.all()  # Usamos el related_name definido en el modelo
    return render(request, 'lista_contactos.html', {'anciano': anciano, 'contactos': contactos})

# Crear un nuevo contacto para un anciano
def crear_contacto(request, anciano_id):
    anciano = get_object_or_404(Anciano, id=anciano_id)
    if request.method == 'POST':
        nombre_familiar = request.POST.get('nombre_familiar')
        relacion = request.POST.get('relacion')
        numero_telefono = request.POST.get('numero_telefono')
        
        # Crear el contacto
        ContactoEmergencia.objects.create(
            anciano=anciano,
            nombre_familiar=nombre_familiar,
            relacion=relacion,
            numero_telefono=numero_telefono
        )
        
        # Redirigir a la lista de contactos del anciano
        return redirect('lista_contactos', anciano_id=anciano.id)

    return render(request, 'crear_contacto.html', {'anciano': anciano})

# Editar un contacto
def editar_contacto(request, id):
    contacto = get_object_or_404(ContactoEmergencia, id=id)
    if request.method == 'POST':
        contacto.nombre_familiar = request.POST.get('nombre_familiar')
        contacto.relacion = request.POST.get('relacion')
        contacto.numero_telefono = request.POST.get('numero_telefono')
        contacto.save()
        return redirect('lista_contactos', anciano_id=contacto.anciano.id)
    return render(request, 'editar_contacto.html', {'contacto': contacto})

# Eliminar un contacto
def eliminar_contacto(request, id):
    contacto = get_object_or_404(ContactoEmergencia, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos', anciano_id=contacto.anciano.id)
    return render(request, 'eliminar_contacto.html', {'contacto': contacto})

#---------Enfermedades--------------------------------------------------

def lista_enfermedades_todas(request):
    enfermedades = Enfermedad.objects.all()  # Obtiene todas las enfermedades
    return render(request, 'lista_enfermedades.html', {'enfermedades': enfermedades})

# Listar enfermedades de un anciano
def lista_enfermedades(request, anciano_id):
    anciano = get_object_or_404(Anciano, id=anciano_id)
    enfermedades = Enfermedad.objects.filter(anciano=anciano)
    
    return render(request, 'lista_enfermedades.html', {
        'anciano': anciano,
        'enfermedades': enfermedades
    })


def crear_enfermedad(request, anciano_id):
    anciano = get_object_or_404(Anciano, id=anciano_id)

    if request.method == 'POST':
        nombre_enfermedad = request.POST.get('nombre_enfermedad')
        fecha_diagnostico = request.POST.get('fecha_diagnostico')

        # Crear nueva enfermedad
        Enfermedad.objects.create(anciano=anciano, nombre_enfermedad=nombre_enfermedad, fecha_diagnostico=fecha_diagnostico)
        
        # Volver a la misma página para agregar otra enfermedad
        return redirect(reverse('crear_enfermedad', kwargs={'anciano_id': anciano.id}))

    return render(request, 'crear_enfermedad.html', {'anciano': anciano})

# Editar una enfermedad
def editar_enfermedad(request, id):
    enfermedad = get_object_or_404(Enfermedad, id=id)
    if request.method == 'POST':
        enfermedad.nombre_enfermedad = request.POST.get('nombre_enfermedad')
        enfermedad.fecha_diagnostico = request.POST.get('fecha_diagnostico')
        enfermedad.save()
        return redirect('lista_enfermedades', anciano_id=enfermedad.anciano.id)
    return render(request, 'editar_enfermedad.html', {'enfermedad': enfermedad})

# Eliminar una enfermedad
def eliminar_enfermedad(request, id):
    enfermedad = get_object_or_404(Enfermedad, id=id)
    if request.method == 'POST':
        enfermedad.delete()
        return redirect('lista_enfermedades', anciano_id=enfermedad.anciano.id)
    return render(request, 'eliminar_enfermedad.html', {'enfermedad': enfermedad})