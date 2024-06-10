from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Disciplina, Projeto
from .forms import DisciplinaForm, ProjetoForm
from django.contrib.auth.decorators import login_required

def lista_projetos(request):
    userPerm = request.user.groups.filter(name = 'Editores de Curso').exists() or request.user.is_superuser
    projetos = Projeto.objects.all()
    return render(request, 'appcurso/projetos.html', {'projetos': projetos,'userPerm': userPerm})

def curso_view(request):
    userPerm = request.user.groups.filter(name = 'Editores de Curso').exists() or request.user.is_superuser


    curso = Curso.objects.first()  # Pode ajustar de acordo com sua lógica
    return render(request, 'appcurso/curso.html', {'curso': curso,'userPerm': userPerm})

def disciplinas_view(request):
    userPerm = request.user.groups.filter(name = 'Editores de Curso').exists() or request.user.is_superuser


    disciplinas = Disciplina.objects.all()
    disciplinas_por_ano_e_semestre = {}

    for disciplina in disciplinas:
        ano = disciplina.ano
        semestre = disciplina.semestre
        if ano not in disciplinas_por_ano_e_semestre:
            disciplinas_por_ano_e_semestre[ano] = {}
        if semestre not in disciplinas_por_ano_e_semestre[ano]:
            disciplinas_por_ano_e_semestre[ano][semestre] = []
        disciplinas_por_ano_e_semestre[ano][semestre].append(disciplina)

    context = {'disciplinas_por_ano_e_semestre': disciplinas_por_ano_e_semestre,'userPerm': userPerm}
    return render(request, 'appcurso/disciplinas.html', context)



def disciplina_view(request,disciplina_id):
    userPerm = request.user.groups.filter(name = 'Editores de Curso').exists() or request.user.is_superuser

    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    projeto = Projeto.objects.filter(disciplina=disciplina)
    context = {'disciplina': disciplina, 'projetos':projeto,'userPerm': userPerm}
    return render(request, "appcurso/disciplina.html", context)

def projeto_view(request, projeto_id):
    userPerm = request.user.groups.filter(name = 'Editores de Curso').exists() or request.user.is_superuser

    projeto = get_object_or_404(Projeto, id=projeto_id)
    return render(request, 'appcurso/projeto.html', {'projeto': projeto,'userPerm': userPerm})


@login_required
def adicionar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appcurso:lista_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'appcurso/adicionar_disciplina.html', {'form': form})

@login_required
def adicionar_projeto(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.disciplina = disciplina
            projeto.save()
            return redirect('appcurso:disciplina', disciplina_id=disciplina_id)
    else:
        form = ProjetoForm(initial={'disciplina': disciplina_id})
    return render(request, 'appcurso/adicionar_projeto.html', {'form': form, 'disciplina': disciplina})



@login_required
def editar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('appcurso:disciplina', disciplina_id=disciplina_id)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'appcurso/editar_disciplina.html', {'form': form, 'disciplina': disciplina})






@login_required
def editar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('appcurso:projeto', projeto_id=projeto_id)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'appcurso/editar_projeto.html', {'form': form, 'projeto': projeto})











@login_required
def add_lista_projetos(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('appcurso:lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'appcurso/adicionar_lista_projeto.html', {'form': form})