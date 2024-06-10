from django.shortcuts import render, get_object_or_404, redirect
from .models import Banda, Album, Musica
from django.contrib.auth.decorators import login_required
from .forms import BandaForm, AlbumForm, MusicaForm

def html_css_view(request):
    return render(request, 'bandas/html5-css.html')

def _bandas_view(request):
    userPerm = request.user.groups.filter(name = 'Editores de Bandas').exists() or request.user.is_superuser


    bandas = Banda.objects.all()
    context = {'bandas': bandas,'userPerm': userPerm}
    return render(request, "bandas/bandas.html", context)

def _banda_view(request, banda_id):
    userPerm = request.user.groups.filter(name = 'Editores de Bandas').exists() or request.user.is_superuser

    banda = get_object_or_404(Banda, id=banda_id)
    albuns = Album.objects.filter(banda=banda)
    context = {'banda': banda, 'albuns': albuns,'userPerm': userPerm}
    return render(request, "bandas/banda.html", context)

def _album_view(request, album_id):
    userPerm = request.user.groups.filter(name = 'Editores de Bandas').exists() or request.user.is_superuser

    album = get_object_or_404(Album, id=album_id)
    context = {'album': album,'userPerm': userPerm}
    return render(request, "bandas/album.html", context)

def _musica_view(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    album_id = None
    for album in Album.objects.all():
        if musica in album.musicas.all():
            album_id = album.id
            break
    context = {'musica': musica, 'album_id': album_id}
    return render(request, "bandas/musica.html", context)



@login_required
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:lista_bandas')  # Redireciona para a página inicial de bandas

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

# Create your views here.


@login_required
def novo_album(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.banda = banda  # Definindo a banda do álbum como a banda atual
            album.save()
            return redirect('bandas:banda', banda_id=banda_id)
    else:
        form = AlbumForm(initial={'banda': banda_id})  # Definindo a banda inicial do formulário como a banda atual
    return render(request, 'bandas/novo_album.html', {'form': form, 'banda': banda})


@login_required
def nova_musica(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.save()
            album.musicas.add(musica)
            return redirect('bandas:album', album_id=album_id)
    else:
        form = MusicaForm()
    return render(request, 'bandas/nova_musica.html', {'album': album, 'form': form})



@login_required
def confirm_delete_banda(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    if request.method == 'POST':
        banda.delete()
        return redirect('bandas:lista_bandas')  # Redireciona para a página inicial de bandas após a exclusão
    return render(request, 'bandas/confirm_delete_banda.html', {'banda': banda})

@login_required
def confirm_delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == 'POST':
        album.delete()
        return redirect('bandas:banda', banda_id=album.banda.id)

    return render(request, 'bandas/confirm_delete_album.html', {'album': album})

@login_required
def confirm_delete_musica(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    album_id = request.GET.get('album_id')

    if request.method == 'POST':
        if 'confirm' in request.POST:
            album = get_object_or_404(Album, pk=album_id)
            album.musicas.remove(musica)  # Remove a música do álbum
            musica.delete()
            return redirect('bandas:album', album_id=album_id)

    return render(request, 'bandas/confirm_delete_musica.html', {'musica': musica, 'album_id': album_id})


@login_required
def editar_banda(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES , instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda', banda_id=banda_id)
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/editar_banda.html', {'form': form, 'banda': banda})



@login_required
def editar_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES , instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album', album_id=album_id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'bandas/editar_album.html', {'form': form, 'album': album})


@login_required
def editar_musica(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musica', musica_id=musica_id)
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'bandas/editar_musica.html', {'form': form, 'musica': musica})