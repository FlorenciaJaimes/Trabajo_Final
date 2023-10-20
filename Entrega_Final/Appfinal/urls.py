from django.urls import path
from Appfinal.views import (inicio, cargar_estilo, cargar_ingredientes, buscar_estilo,
                            ipa, scotish, apa, ver_BD, delete_estilo, edit_estilo, golden,
                            blog, nosotros, receta_blonde, receta_ipa, receta_porter, login_request,
                            registrarse, editarPerfil)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/',  inicio, name="Inicio"),
    path('cargarEstilo/', cargar_estilo, name="CargarEstilo" ),
    path('cargarIngredientes/', cargar_ingredientes, name="CargarIngredientes" ),
    path('buscarEstilo/', buscar_estilo, name="BuscarEstilo" ),
    path('verBD/', ver_BD, name="VerBD" ),
    path('blog/', blog, name="Blog" ),
    path('nosotros/', nosotros, name="Nosotros" ),
    path('ipa/', ipa, name="Ipa" ),
    path('apa/', apa, name="Apa" ),
    path('scotish/', scotish, name="Scotish" ),
    path('golden/', golden, name="Golden" ),
    path('recetablonde/', receta_blonde, name="RecetaBlonde" ),
    path('recetaipa/', receta_ipa, name="RecetaIpa" ),
    path('recetaporter/', receta_porter, name="RecetaPorter" ),
    path('deleteEstilo/<int:estilo_id>', delete_estilo, name="DeleteEstilo" ),
    path('editarEstilo/<int:estilo_id>', edit_estilo, name="EditarEstilo" ),
]

urlpatterns += [
    path('login/', login_request, name="Login"),
    path('registrarse/', registrarse, name='Registrarse'),
    path('editarPerfil/', editarPerfil, name='EditarPerfil'),
    path('logout/', LogoutView.as_view(
        template_name='Appfinal/logout.html'), name='Logout'),
    

]
