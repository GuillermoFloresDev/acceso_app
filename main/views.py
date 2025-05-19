# main/views.py
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cerrar_sesion(request):
    request.session.flush()
    return redirect('inicio')


def inicio(request):
    if request.method == 'POST':
        celular = request.POST.get('celular')
        try:
            usuario = Usuario.objects.get(numero_celular=celular)
            request.session['usuario_id'] = usuario.id
            return redirect('validar_usuario')
        except Usuario.DoesNotExist:
            messages.error(request, 'Número de celular no encontrado.')
    
    return render(request, 'main/inicio.html')

def validar_usuario(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('inicio')

    usuario = Usuario.objects.get(id=usuario_id)

    if request.method == 'POST':
        if 'es_el' in request.POST:
            return redirect('tomar_foto')
        else:
            request.session.flush()
            return redirect('inicio')

    return render(request, 'main/validar.html', {'usuario': usuario})

def tomar_foto(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('inicio')
    
    usuario = Usuario.objects.get(id=usuario_id)

    if request.method == 'POST':
        foto = request.FILES.get('foto')
        if foto:
            usuario.foto = foto
            usuario.save()
            messages.success(request, '¡Foto guardada correctamente!')
            request.session.flush()
            return redirect('inicio')

    return render(request, 'main/foto.html', {'usuario': usuario})
