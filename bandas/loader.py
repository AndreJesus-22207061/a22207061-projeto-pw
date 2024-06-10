from bandas.models import *
import json



Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

albums_info = []
bandas_info = []



with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)


    for banda in bandas:
        banda_info = {
            "nome": banda["nome"],
            "genero": banda["genero"],
            "nacionalidade": banda["nacionalidade"],
            "ano_criacao": banda["ano_criacao"]
        }
        bandas_info.append(banda_info)


        Banda.objects.create(
            nome = banda["nome"],
            genero =  banda["genero"],
            nacionalidade = banda["nacionalidade"],
            ano_criacao = banda["ano_criacao"]
        )


with open('bandas/json/discos.json') as f:

    albuns = json.load(f)



    for album_info in albuns:
        album = Album.objects.create(
            nome=album_info['nome'],
            ano_lancamento=album_info['ano_lancamento'],
            banda = Banda.objects.get(nome = album_info["banda"])
        )

        for musica_info in album_info['musicas']:
            musica = Musica.objects.create(
                nome=musica_info['nome'],
                tempo=musica_info['tempo'],
                spotify_link=musica_info['spotify_link']
            )
            album.musicas.add(musica)

