
from django.urls import path, include
from .views import eliminardatos, index, login, crearcuenta, cogerdatos, editpage, cogerdatosnuevos, redireccionarlogin, redireccionindex


urlpatterns = [
    path("", index, name="index"),
    path("login/", login , name="login"),
    path("redireccionindex/", redireccionindex, name="usuario"),
    path("cuenta/", crearcuenta, name="account"),
    path("redireccion/", redireccionarlogin, name="redireccionlogin"),
    path("datos/", cogerdatos, name="data"),
    path('eliminardatos/<int:id_table>/', eliminardatos, name="borrar"),
    path("editar/<int:id_table>/", editpage, name="editar"),
    path("nuevo/<int:id_table>", cogerdatosnuevos, name="nuevo")
]

