from django import forms
from .models import Artigo, Autor

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={
          'placeholder':'Titulo do Artigo',
            }),
            'conteudo': forms.Textarea(attrs={
          'placeholder':'Conteúdo do Artigo',
            }),
        }



class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
          'placeholder':'Nome do Autor',
            }),
            'idade': forms.TextInput(attrs={
          'placeholder':'Idade do Autor',
            }),
            'email': forms.TextInput(attrs={
          'placeholder':'Email do Autor',
            }),
        }