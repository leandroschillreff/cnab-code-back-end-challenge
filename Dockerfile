# Dockerfile

# fazendo o pull da imagem oficial no Docker Hub
FROM python:3.11

# setando variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# executando a instalação dos pacotes

# definindo o diretório de trabalho no contêiner
WORKDIR /django_app

# copiando todos os arquivos para o diretório de trabalho
COPY . /django_app/

# atualizando o pip e instalando requerimentos
RUN pip install -U pip
RUN pip install -r requirements.txt