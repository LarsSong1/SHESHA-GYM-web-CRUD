import sqlite3 as sql
from django.shortcuts import render, redirect
from .models import comentario, register_data
from django.http import HttpResponse


# Create your views here.
def index(request):
    com = comentario.objects.all()
    return render(request, "index.html", {"texto": com})


def login(request):
    return render(request, "login.html")


def crearcuenta(request):
    return render(request, "register.html")

def redireccionarlogin(request):
    nombre = request.POST["usuario"]
    contraseña = request.POST["contraseña"]
    conf_contraseña = request.POST["confirmar"]
    if contraseña == conf_contraseña:
        usuario = register_data(nombre_usuario = nombre, contraseña_usuario = contraseña, verificacion_contraseña = conf_contraseña)
        d_b = "registro.db"
        coneccion = sql.connect(d_b)
        cursor = coneccion.cursor()
        cursor.execute("SELECT nombre_usuario FROM sheshagym_register_data")
        nicks = cursor.fetchall()
        for user in nicks:
            if nombre in user:
                template = """
                    <div style="width:100vw; height:100vh; display:flex; flex-direction: column; justify-content:center; align-items:center; background-color: #101010;">
                        <h2 style="color: #FFDF5B">Registro ocupado</h2>
                        <h1 style="color: #FFDF5B">El usuario ya existe en el sistema</h1>
                        <h4 style="color: #FEFEFE";>Vuelva e intente de nuevo</h4>
                        
                    </div>
                """
                return HttpResponse(template)
            else:
                usuario.save()
                return render(request, "login.html", {"usuarios": usuario})
        
    else:
        return render(request, "error.html")
    


def redireccionindex(request):
    nombre = request.POST["usuario"]
    contraseña = request.POST["contraseña"]
    d_b = "registro.db"
    coneccion = sql.connect(d_b)
    cursor = coneccion.cursor()
    cursor.execute("SELECT nombre_usuario FROM sheshagym_register_data")
    nicks = cursor.fetchall()
    cursor.execute("SELECT contraseña_usuario FROM sheshagym_register_data")
    nicks_password = cursor.fetchall()
    for user in nicks:
        if nombre in user:
            print("si esta el u")
    
    for user_password in nicks_password:
            print("si esta la contraseña")
            
    if nombre in user:
        if contraseña in user_password:
            return render(request, "index.html", {"usuario": user})

        else:
            template = """
                        <div style="width:100vw; height:100vh; display:flex; flex-direction: column; justify-content:center; align-items:center; background-color: #101010;">
                            <h2 style="color: #FFDF5B">login invalido</h2>
                            <h1 style="color: #FFDF5B">Contraseña incorrecta</h1>
                            <h4 style="color: #FEFEFE";>Vuelva e intente de nuevo</h4>
                            
                        </div>
                    """
            return HttpResponse(template)
                
    else:
        template = """
                    <div style="width:100vw; height:100vh; display:flex; flex-direction: column; justify-content:center; align-items:center; background-color: #101010;">
                        <h2 style="color: #FFDF5B">login invalido</h2>
                        <h1 style="color: #FFDF5B">El usuario no existe en el sistema</h1>
                        <h4 style="color: #FEFEFE";>Vuelva e intente de nuevo</h4>
                        
                    </div>
                """
        return HttpResponse(template)


def eliminardatos(request, id_table):
    eliminar = comentario.objects.get(id=id_table)
    eliminar.delete()
    return  redirect("index")

def cogerdatos(request):
    texto = comentario(texto = request.POST["texto_usuario"])
    texto.save()
    return redirect("index")


def editpage(request, id_table):
    eliminar = comentario.objects.get(id=id_table)
    print(eliminar)
    return render(request, "edit.html", {"id": eliminar})


def cogerdatosnuevos(request, id_table):
    eliminar = comentario.objects.get(id=id_table)
    print(eliminar.id)
    d_b = "registro.db"
    coneccion = sql.connect(d_b)
    cursor = coneccion.cursor()
    nuevodato= comentario(texto = request.POST["nuevo_dato"])
    cursor.execute(f"UPDATE sheshagym_comentario SET texto = '{nuevodato.texto}' where id = {eliminar.id}")
    coneccion.commit()
    coneccion.close()
    # nuevodato.save()
    print(nuevodato)
    return redirect("index")



  




    
    
    