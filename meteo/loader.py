import os
import zipfile

# Caminho para o arquivo ZIP (relativo ao diretório do script)
zip_file_path = 'static/meteo/icons_ipma_weather.zip'

# Diretório de destino para extrair os arquivos
extract_to_path = 'static/meteo'

# Verifique se o diretório de destino existe, se não, crie-o
if not os.path.exists(extract_to_path):
    os.makedirs(extract_to_path)

# Função para descompactar o arquivo ZIP
def descompactar_arquivo(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f'Arquivos extraídos para {extract_path}')

# Chamada da função para descompactar o arquivo
descompactar_arquivo(zip_file_path, extract_to_path)