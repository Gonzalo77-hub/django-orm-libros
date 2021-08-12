from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('libros', views.crear_libro),
    path('books/<int:val>', views.rutas),
    path('authors', views.index2),
    path('authors/<int:val>', views.rutas2),
    path('crear', views.crear_autor),
    path('asociar_libro', views.asociar_lib),
    path('asociar_autor', views.asociar_aut),

]
