from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Autor, Comentario
from .forms import ArtigoForm, AutorForm
from django.contrib.auth.decorators import login_required

def artigos(request):
    userPerm = request.user.groups.filter(name = 'Editores de Artigos').exists() or request.user.is_superuser
    artigos = Artigo.objects.all()
    return render(request, 'blogues/artigos.html', {'artigos': artigos,'userPerm': userPerm})



def artigo(request, id):
    userPerm = request.user.groups.filter(name = 'Editores de Artigos').exists() or request.user.is_superuser
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = Comentario.objects.filter(artigo=artigo)
    return render(request, 'blogues/artigo.html', {'artigo': artigo, 'comentarios': comentarios,'userPerm': userPerm})



def autores(request):
    userPerm = request.user.groups.filter(name = 'Editores de Artigos').exists() or request.user.is_superuser
    autores = Autor.objects.all()
    return render(request, 'blogues/autores.html', {'autores': autores,'userPerm': userPerm})



def autor(request, id):
    userPerm = request.user.groups.filter(name = 'Editores de Artigos').exists() or request.user.is_superuser
    autor = get_object_or_404(Autor, id= id)
    artigos = Artigo.objects.filter(autor=autor)
    return render(request, 'blogues/autor.html', {'autor': autor, 'artigos': artigos,'userPerm': userPerm})




@login_required
def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogues:artigos')
    else:
        form = ArtigoForm()

    return render(request, 'blogues/criar_artigo.html', {'form': form})

@login_required
def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogues:autores')
    else:
        form = AutorForm()

    return render(request, 'blogues/criar_autor.html', {'form': form})



@login_required
def confirm_delete_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == 'POST':
        artigo.delete()
        return redirect('blogues:artigos')  # Redireciona para a página inicial de bandas após a exclusão
    return render(request, 'blogues/confirm_delete_artigo.html', {'artigo': artigo})



@login_required
def confirm_delete_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('blogues:autores')  # Redireciona para a página inicial de bandas após a exclusão
    return render(request, 'blogues/confirm_delete_autor.html', {'autor': autor})





@login_required
def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST,request.FILES , instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('blogues:artigo', id=artigo_id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'blogues/editar_artigo.html', {'form': form, 'artigo': artigo})


@login_required
def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST,request.FILES , instance=autor)
        if form.is_valid():
            form.save()
            return redirect('blogues:autor', id=autor_id)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'blogues/editar_autor.html', {'form': form, 'autor': autor})
