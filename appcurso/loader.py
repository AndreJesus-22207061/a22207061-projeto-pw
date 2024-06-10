import json
from appcurso.models import *

Curso.objects.all().delete()
AreaCientifica.objects.all().delete()
LinguagemDeProgramacao.objects.all().delete()
Disciplina.objects.all().delete()
Projeto.objects.all().delete()
Docente.objects.all().delete()

def importar_curso(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    #------------------------------------------------- Importar cursos--------------------------------------------------------------------
    cursos_data = data.get('cursos', [])
    for curso_data in cursos_data:
        print(f"Nome: {curso_data['nome']}")
        print(f"Apresentacao: {curso_data['apresentacao']}")
        print(f"Objetivos: {curso_data['objetivos']}")
        print(f"Competencias: {curso_data['competencias']}")


        Curso.objects.create(
            nome = curso_data['nome'],
            apresentacao = curso_data['apresentacao'],
            objetivos = curso_data['objetivos'],
            competencias = curso_data['competencias']
        )

    #-------------------------------------------- Importar áreas científicas-------------------------------------------------------------------
    areas_cientificas_data = data.get('areas_cientificas', [])
    for area_data in areas_cientificas_data:
        print(area_data['nome'])

        AreaCientifica.objects.create(nome = area_data['nome'])

    #----------------------------------------Importar linguagens de programação--------------------------------------------------------------
    linguagens_data = data.get('linguagens_programacao', [])
    for linguagem_data in linguagens_data:
        print(linguagem_data['nome'])

        LinguagemDeProgramacao.objects.create(nome = linguagem_data['nome'])

    #------------------------------------- ---------Importar disciplinas---------------------------------------------------------------------
    disciplinas_data = data.get('disciplinas', [])
    for disciplina_data in disciplinas_data:

        disciplina_linguagens = disciplina_data.pop('linguagens', [])
        area_cientifica_nome = disciplina_data.pop('area_cientifica')

        print(f"Nome: {disciplina_data['nome']}")
        print(f"Ano: {disciplina_data['ano']}")
        print(f"Semestre: {disciplina_data['semestre']}")
        print(f"ECTS: {disciplina_data['ects']}")
        print(f"Apresentação: {disciplina_data['apresentacao']}")
        print(f"Programa: {disciplina_data['programa']}")
        print(f"CurricularIUnitReadableCode: {disciplina_data['curricularIUnitReadableCode']}")
        print("Linguagens:")

        for linguagem in disciplina_linguagens:
            print(f"- {linguagem}")

        disciplina = Disciplina.objects.create(
            nome = disciplina_data['nome'],
            ano = disciplina_data['ano'],
            semestre = disciplina_data['semestre'],
            ects = disciplina_data['ects'],
            apresentacao = disciplina_data['apresentacao'],
            programa = disciplina_data['programa'],
            curricularIUnitReadableCode = disciplina_data['curricularIUnitReadableCode'],
        )


        area_cientifica = AreaCientifica.objects.get(nome=area_cientifica_nome)
        disciplina.area_cientifica = area_cientifica


        disciplina.linguagens.set(LinguagemDeProgramacao.objects.filter(nome__in=disciplina_linguagens))
        disciplina.save()
    # ----------------------------------- ------------Importar projetos ----------------------------------------------------------------------------------
    projetos_data = data.get('projetos', [])
    for projeto_data in projetos_data:
        projeto_linguagens = projeto_data.pop('linguagens', [])
        projeto_disciplina = projeto_data.pop('disciplina', None)

        print(f"Nome: {projeto_data['nome']}")
        print(f"Descrição: {projeto_data['descricao']}")
        print(f"Conceitos Aplicados: {projeto_data['conceitos_aplicados']}")
        print(f"Tecnologias Usadas: {projeto_data['tecnologias_usadas']}")
        print(f"Foto: {projeto_data['foto']}")
        print(f"Vídeo YouTube Link: {projeto_data['video_youtube_link']}")
        print(f"Project Link: {projeto_data['project_link']}")
        print("Linguagens:")

        for linguagem in projeto_linguagens:
            print(f"- {linguagem}")

        if projeto_disciplina:
            print(f"Disciplina: {projeto_disciplina}")

        projeto = Projeto.objects.create(
            nome=projeto_data['nome'],
            descricao=projeto_data['descricao'],
            conceitos_aplicados=projeto_data['conceitos_aplicados'],
            tecnologias_usadas=projeto_data['tecnologias_usadas'],
            foto_project = projeto_data['foto'],
            video_link=projeto_data['video_youtube_link'],
            project_link=projeto_data['project_link']
        )


        projeto.linguagens.set(LinguagemDeProgramacao.objects.filter(nome__in=projeto_linguagens))


        if projeto_disciplina:
            projeto.disciplina = Disciplina.objects.get(nome=projeto_disciplina)
        projeto.save()
    #-------------------------------------------------Importar docentes-------------------------------------------------------------------------
    docentes_data = data.get('docentes', [])
    for docente_data in docentes_data:
        docente_disciplinas = docente_data.pop('disciplinas', [])

        print(f"Nome: {docente_data['nome']}")
        print("Disciplinas:")

        for disciplina in docente_disciplinas:
            print(f"- {disciplina}")

        docente = Docente.objects.create(nome=docente_data['nome'])
        docente.disciplinas.set(Disciplina.objects.filter(nome__in=docente_disciplinas))

    print('Concluio o import')