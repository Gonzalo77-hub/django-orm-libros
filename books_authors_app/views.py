from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    context = {
        'Libros' : Book.objects.all(),}

    return render(request, 'index.html', context)


def crear_libro(request):

    book = Book.objects.create(
        title =  request.POST['titulo_libro'],  
        desc = request.POST['descripcion_libro'])
    return redirect("/")

def rutas(request, val):
        context = {'Libro' : Book.objects.get(id=val),
                    'Autores':Book.objects.get(id=val).Autores.all(),
                    'Autores_1':Author.objects.all() }
        return render(request, 'Books.html', context)
    
def index2(request):
    context = {'Autores' : Author.objects.all()
    }
    return render(request, 'index2.html', context)

def crear_autor(request):

    Autor = Author.objects.create(
        first_name =  request.POST['nombre'],  
        last_name =  request.POST['apellido'],  
        notas = request.POST['notas'])
    return redirect("/authors")

def rutas2(request, val):
        context = {'autor' : Author.objects.get(id=val),
                    'Libros': Author.objects.get(id=val).Books.all(),
                    'Libros_1':Book.objects.all()}
        return render(request, 'Autores.html', context)

def asociar_lib(request):
    id_libro = request.POST['agregar_libro']
    id_autor = request.POST['id_autor']
    libro = Book.objects.get(id=id_libro)
    autor = Author.objects.get(id=id_autor)
    asociacion = autor.Books.add(libro)
    return redirect(f"/authors/{id_autor}")

def asociar_aut(request):
    id_libro = request.POST['id_libro']
    id_autor = request.POST['Autores']
    libro = Book.objects.get(id=id_libro)
    autor = Author.objects.get(id=id_autor)
    asociacion = libro.Autores.add(autor)
    return redirect(f"/books/{id_libro}")




