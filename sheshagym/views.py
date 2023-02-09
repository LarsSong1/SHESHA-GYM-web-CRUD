from re import X
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
    else:
        return render(request, "error.html")
    

    d_b = "registro.db"
    coneccion = sql.connect(d_b)
    cursor = coneccion.cursor()
    cursor.execute("SELECT * FROM sheshagym_register_data")
    x = cursor.fetchall()
    template = """
                    <div style="width:100vw; height:100vh; display:flex; flex-direction: column; justify-content:center; align-items:center; background-color: #101010;">
                        <h2 style="color: #FFDF5B">Registro ocupado</h2>
                        <h1 style="color: #FFDF5B">El usuario ya existe en el sistema</h1>
                        <h4 style="color: #FEFEFE";>Vuelva e intente de nuevo</h4>
                        
                    </div>
                """
    for i in x:
        if nombre in i:
            print("yes")
            return HttpResponse(template)
    
    else:
        usuario.save()
        return render(request, "login.html", {"usuarios": usuario})

        
    


def redireccionindex(request):
    nombre = request.POST["usuario"]
    contraseña = request.POST["contraseña"]
    d_b = "registro.db"
    coneccion = sql.connect(d_b)
    cursor = coneccion.cursor()
    cursor.execute("SELECT * FROM sheshagym_register_data")
    users = cursor.fetchall()
    for user in users:
        if nombre in user:
            print("yes c")
            if contraseña in user:
                print("yes b")
                return render(request, "index.html", {"usuario": user,"user": nombre})
            else:
                template = """
                            <div style="width:100vw; height:100vh; display:flex; flex-direction: column; justify-content:center; align-items:center; background-color: #101010;">
                                <h2 style="color: #FFDF5B">login invalido</h2>
                                <h1 style="color: #FFDF5B">El usuario o contaseña esta mal</h1>
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



  




    
    
    