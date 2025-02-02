# Usar a imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o conteúdo do diretório atual para o diretório de trabalho do container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta que o Streamlit vai usar
EXPOSE 8501

# Definir o comando para rodar a aplicação com Streamlit
CMD ["streamlit", "run", "app.py"]
