from django.shortcuts import render
from .models import Alumno, Genero

# Create your views here.
def index(request):
    alumnos=Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    alumnos=Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def crud(request):
    alumnos=Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)


def alumnosAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=apaterno,
            apellido_materno=amaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,  # Asociar el genero correctamente
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
        )
        obj.save()
        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'alumnos/alumnos_add.html', context)

def alumnos_del(request, pk):
    
    context={}
    try:
     alumno=Alumno.objects.get(rut=pk)
     alumno.delete()
     mensaje='Datos Eliminados'
     alumnos=Alumno.objects.all()
     context={"alumnos":alumnos, "mensaje": mensaje}
     return render(request, 'alumnos/alumnos_list.html', context)
    except:
     mensaje="Error, no existe el rut..."
     alumnos=Alumno.objects.all()
     context={"alumnos":alumnos, "mensaje": mensaje}
     return render(request, 'alumnos/alumnos_list.html', context)