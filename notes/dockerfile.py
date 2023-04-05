# FROM python:3.8-slim-buster
    # imagem base do container 
    # imagem oficial do python 3.8 (mais leve) baseada no S.O debian buster
    # vantagens: possui apenas o essencial para para exc. um projeto em python 

# WORKDIR /app
    # define um dir dentro do container 
    # qualquer comando executado será a partir do /app 

# COPY requirements.txt . 
    # copia o arquivo de requirements do diretório atual (origem = .) para o container

# RUN pip install --no-cache-dir -r requirements.txt
    # da run no container executando um pip install nos requirements 
    # utilizando --no-cache-dir que ajuda a manter o tamanho da imagem menor 

# COPY . .
    # monta todo o diretório atual (origem) para o dir /app do container 

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
    # comando padrão para iniciar o container sempre e subir a FastAPI 
    # webserver uvicorn para rodar o app FastAPI 
    # na porta 5000
    # o parâmetro --host define o endereço IP que o servidor web deve usar para se comunicar com outras máquinas (localhost)
    # "0.0.0.0" significa que ele deve usar o endereço IP padrão do contêiner.


# mais sobre "0.0.0.0"
    # significa "qualquer endereço ou todos os endereços"
    # ao contrário do 127.0.0.1, que é um endereço IP reservado para a interface de loopback
    # o "0.0.0.0" é um endereço que se refere a todas as interfaces de rede disponíveis
    # provê facilidade e flexibilidade as aplicações 