import requests
from django.shortcuts import render
from django.http import JsonResponse

def tempo_lisboa(request):
    previsaoLisboa_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

#--------------------------------------------------(Extrair tipos de Tempo)-----------------------------------------------------------------------
    previsao_response = requests.get(previsaoLisboa_url)
    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsao_hoje = dic_previsao['data'][0]  # Guarda o primeiro dicionário do JSON que é o do dia de hoje
    else:
        previsao_hoje = {}

#--------------------------------------------------(Extrair tipos de Tempo)---------------------------------------------------------------------------




    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])  # Acesse a lista de tipos de tempo
        weather_types = {item['idWeatherType']: item for item in weather_types_list}  # Cria o dicionário chave: idWeather | objeto todo
    else:
        weather_types = {}

 #--------------------------------------------------(Extrair variaveis precisas)---------------------------------------------------------------------------


    city_name = "Lisboa"
    min_temp = previsao_hoje.get('tMin', 'N/A')
    max_temp = previsao_hoje.get('tMax', 'N/A')
    dataDeHoje = previsao_hoje.get('forecastDate', 'N/A')
    weather_type_id = previsao_hoje.get('idWeatherType', 'N/A')
    weather_description = weather_types.get(weather_type_id, {}).get('descWeatherTypePT', 'N/A')

#--------------------------------------------------(Procurar foto relativa ao tempo)---------------------------------------------------------------------------

    icon_filename = f"w_ic_d_{weather_type_id:02d}anim.svg"
    icon_url = f"/static/meteo/{icon_filename}"

#---------------------------------------------------------------------------------------------------------------------------------------------
    context = {
        'cidade': city_name,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'dataDeHoje': dataDeHoje,
        'descricaoTempo': weather_description,
        'icon_url': icon_url,
    }

    return render(request, 'meteo/tempo_lisboa.html', context)



#=============================================================================================================================================




def previsao_proximos_5dias(request):
    cidade_id = 1110600
    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    # Obter previsão do tempo para os próximos 5 dias
    previsao_response = requests.get(previsao_url)
    if previsao_response.status_code == 200:
        previsao_data = previsao_response.json()['data'][:5]  # Pegando apenas os próximos 5 dias
    else:
        previsao_data = []

    # Obter tipos de tempo
    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}
    else:
        weather_types = {}


    proximos_5dias = []
    for dia in previsao_data:
        data = dia.get('forecastDate', 'N/A')
        min_temp = dia.get('tMin', 'N/A')
        max_temp = dia.get('tMax', 'N/A')
        weather_type_id = dia.get('idWeatherType', 'N/A')
        weather_description = weather_types.get(weather_type_id, {}).get('descWeatherTypePT', 'N/A')
        icon_filename = f"w_ic_d_{weather_type_id:02d}anim.svg"
        icon_url = f"/static/meteo/{icon_filename}"

        proximos_5dias.append({
            'data': data,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'descricaoTempo': weather_description,
            'icon_url': icon_url
        })

    context = {
        'cidade': 'Lisboa',
        'previsao_proximos_5dias': proximos_5dias
    }

    return render(request, 'meteo/previsao_proximos_5dias.html', context)

                                                           # (API)

#---------------------------------------------------(Funcao auxilear)--------------------------------------------------------------------------

def obter_nome_cidade(cidade_id):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cidades_response = requests.get(cidades_url)

    if cidades_response.status_code != 200:
        return "Nome da cidade não disponível"

    dic_cidades = cidades_response.json()
    cidades_data = dic_cidades.get('data', [])

    for cidade in cidades_data:
        if cidade.get('globalIdLocal') == cidade_id:
            return cidade.get('local')

    return "Nome da cidade não disponível"



#---------------------------------------------------(Endpoint Listar cidades)--------------------------------------------------------------------------


def listar_cidades(request):
    cidades_url = 'https://api.ipma.pt/open-data/distrits-islands.json'

    # Faz uma requisição à API para obter a lista de cidades
    cidades_response = requests.get(cidades_url)
    if cidades_response.status_code == 200:
        dic_cidades = cidades_response.json()
        cidades_data = dic_cidades.get('data', [])

    # Extrai as cidades e seus IDs
    cidades = [{"nome": cidade.get('local'), "id": cidade.get('globalIdLocal')} for cidade in cidades_data]

    return JsonResponse({"cidades": cidades})



#--------------------------------------(Endpoint previsao de hoje para cidade x)--------------------------------------------------------------------------

def previsao_hojeAPI(request,cidade_id):

    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'


    previsao_response = requests.get(previsao_url)

    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsao_hoje = dic_previsao['data'][0]


    weather_types_response = requests.get(weather_types_url)

    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}
        weather_description = weather_types.get(previsao_hoje['idWeatherType'], {}).get('descWeatherTypePT', 'Descrição não disponível')

    resposta = {
        "cidade": obter_nome_cidade(cidade_id),
        "data": previsao_hoje.get('forecastDate', 'N/A'),
        "min_temp": previsao_hoje.get('tMin', 'N/A'),
        "max_temp": previsao_hoje.get('tMax', 'N/A'),
        "descricaoTempo": weather_description,
        "precipitacao": previsao_hoje.get('precipitaProb', 'N/A'),
        "icon_url": f"w_ic_d_{previsao_hoje['idWeatherType']:02d}anim.svg"
    }

    return JsonResponse(resposta)

#--------------------------------------(Endpoint previsao de proximos 5 dias para cidade x)----------------------------------------------------------------

def previsao_proximos_5diasAPI(request,cidade_id):

    previsao_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'


    previsao_response = requests.get(previsao_url)

    if previsao_response.status_code == 200:
        dic_previsao = previsao_response.json()
        previsoes = dic_previsao['data'][:5]  # Previsão para os próximos 5 dias


    weather_types_response = requests.get(weather_types_url)

    if weather_types_response.status_code == 200:
        weather_types_data = weather_types_response.json()
        weather_types_list = weather_types_data.get('data', [])
        weather_types = {item['idWeatherType']: item for item in weather_types_list}

    previsao_proximos_5dias = []
    for previsao in previsoes:
        weather_description = weather_types.get(previsao['idWeatherType'], {}).get('descWeatherTypePT', 'Descrição não disponível')
        previsao_proximos_5dias.append({
            "data": previsao.get('forecastDate', 'N/A'),
            "min_temp": previsao.get('tMin', 'N/A'),
            "max_temp": previsao.get('tMax', 'N/A'),
            "descricaoTempo": weather_description,
            "precipitacao": previsao.get('precipitaProb', 'N/A'),
            "icon_url": f"w_ic_d_{previsao['idWeatherType']:02d}anim.svg"
        })

        resposta = {
        "cidade": obter_nome_cidade(cidade_id),
        "previsoes": previsao_proximos_5dias
        }

    return JsonResponse(resposta)




def explicaAPI(request):
    return render(request, 'meteo/explicaAPI.html')


