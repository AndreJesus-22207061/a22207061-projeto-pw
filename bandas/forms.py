from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'

        labels = {
            'nome': 'Nome da Banda',
            'genero': 'Género Musical',
            'nacionalidade': 'Nacionalidade',
            'ano_criacao': 'Ano de Criação',
        }

        widgets = {
            'nome': forms.TextInput(attrs={
          'placeholder':'Nome da Banda',
            }),
            'genero':forms.TextInput(attrs={
            'placeholder':'Género da Banda',
            }),
            'nacionalidade':forms.TextInput(attrs={
            'placeholder':'Nacionalidade da Banda',
            }),
            'ano_criacao':forms.TextInput(attrs={
            'placeholder':'Ano de Criacao da Banda',
            }),
            'biografia':forms.Textarea(attrs={
            'placeholder':'Biografia da Banda',
            }),
            'foto': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }





class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['banda']

        widgets = {
            'nome': forms.TextInput(attrs={
            'placeholder':'Nome do Álbum',
            }),
            'ano_lancamento':forms.TextInput(attrs={
            'placeholder':'Ano Lançamento do Álbum',
            }),
            'capa': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        banda = kwargs.pop('banda', None)  # Obtém o valor da banda do contexto
        super().__init__(*args, **kwargs)
        if banda:
            self.fields['banda'].initial = banda  # Define a banda inicial do formulário


class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
          'placeholder':'Nome da Música',
            }),
            'spotify_link':forms.TextInput(attrs={
            'placeholder':'Link do Spotify',
            }),
            'tempo':forms.TextInput(attrs={
            'placeholder':'Duração "XmXXs"',
            }),
        }