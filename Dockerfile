# -----------------
# Estágio de Build
# -----------------
# Usamos uma imagem oficial do Python como base
FROM python:3.11-slim-bullseye as builder

# Define o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app

# Define variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema necessárias para compilar pacotes Python
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Instala as dependências do Python
# Primeiro copiamos apenas o requirements.txt para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# -----------------
# Estágio Final
# -----------------
# Usamos uma nova imagem base limpa para um contêiner menor e mais seguro
FROM python:3.11-slim-bullseye

# Cria um usuário não-root para rodar a aplicação
RUN addgroup --system app && adduser --system --group app

# Define o diretório de trabalho
WORKDIR /usr/src/app

# Copia as dependências pré-compiladas do estágio de build
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copia o código da aplicação para o contêiner
COPY . .

# Coleta os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Muda a propriedade dos arquivos para o usuário 'app'
# A pasta media será criada dinamicamente, então damos permissão na pasta pai
RUN chown -R app:app /usr/src/app

# Muda para o usuário não-root
USER app

# Expõe a porta 8000 para o Gunicorn
EXPOSE 8000

# Comando para iniciar a aplicação com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
