# Imagen base
FROM python:3.9-slim-buster

# Copiar los archivos de la aplicación al contenedor
COPY . /cv

# Establecer el directorio de trabajo
WORKDIR /cv

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 7000
EXPOSE 7000

# Comando de inicio
CMD ["python", "main.py"]
