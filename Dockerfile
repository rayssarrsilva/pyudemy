FROM python:3.11-slim

WORKDIR /app 

#arquivo de dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copia o restante do código
COPY . . 

# Expõe a porta que o Flask vai rodar
EXPOSE 5000

CMD ["python", "app.py"]