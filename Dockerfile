# Use a imagem oficial do Python como base
FROM python:3.10

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criação do diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante do código para o diretório de trabalho
COPY . /app/



# Executa as migrações e inicia o servidor quando o contêiner for iniciado
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
