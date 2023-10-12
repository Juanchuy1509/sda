# Usa una imagen base de Python
FROM python:3.11.5-alpine3.18

# Establece el directorio de trabajo en /app
WORKDIR /app

COPY ./requirements.txt ./

# Instala las dependencias de tu proyecto (si tienes un archivo requirements.txt)
RUN pip install -r requirements.txt

# Copia los archivos de tu proyecto al directorio de trabajo
COPY . .

# Especifica el comando que se ejecutará cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
