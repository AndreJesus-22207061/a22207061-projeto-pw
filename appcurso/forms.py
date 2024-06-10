from django import forms
from .models import Disciplina, Projeto

class DisciplinaForm(forms.ModelForm):


    ANO_CHOICES = (
        (1, '1º ano'),
        (2, '2º ano'),
        (3, '3º ano'),
    )

    SEMESTRE_CHOICES = (
        (1, '1º semestre'),
        (2, '2º semestre'),
    )

    ano = forms.ChoiceField(choices=ANO_CHOICES)
    semestre = forms.ChoiceField(choices=SEMESTRE_CHOICES)



    class Meta:
        model = Disciplina
        fields = '__all__'  # ou especifique quais campos você quer no formulário

        labels = {
            'nome': 'Nome da Disciplina',
            'ano': 'Ano Curricular da Disciplina',
            'semestre': 'Semestre Curricular da Disciplina',
            'ects': 'ECTS da Disciplina',
        }


        widgets = {
            'nome': forms.TextInput(attrs={
          'placeholder':'Nome da Disciplina',
            }),
            'ects':forms.TextInput(attrs={
            'placeholder':'Número de ECTS',
            }),
            'apresentacao':forms.Textarea(attrs={
            'placeholder':'Apresentação da Disciplina',
            }),
            'programa':forms.Textarea(attrs={
            'placeholder':'Programa da Disciplina',
            }),
            'curricularIUnitReadableCode':forms.TextInput(attrs={
            'placeholder':'Código da Disciplina',
            }),
        }


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome do Projeto',
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'Descrição do Projeto',
            }),
            'conceitos_aplicados': forms.Textarea(attrs={
                'placeholder': 'Conceitos Aplicados no Projeto',
            }),
            'tecnologias_usadas': forms.Textarea(attrs={
                'placeholder': 'Tecnologias Utilizadas no Projeto',
            }),
            'video_link': forms.TextInput(attrs={
                'placeholder': 'Link Video do Projeto',
            }),
            'project_link': forms.TextInput(attrs={
                'placeholder': 'Link do Projeto',
            }),
        }

    def __init__(self, *args, **kwargs):
        disciplina = kwargs.pop('disciplina', None)
        super().__init__(*args, **kwargs)
        if disciplina:
            self.fields['disciplina'].initial = disciplina
