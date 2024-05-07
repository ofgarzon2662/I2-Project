# Módulo de Posts
Este es el componente de Post o Publicaciones de la aplicación. Corre de manera independiente y se comunica con el componente de usuarios para obtener información de los usuarios que han creado las publicaciones.

## Índice

1. [Ejecucion](#Ejecucion)
2. Ejecutar Pruebas con Postman
3. Pruebas Unitarias
4. Autor


## Ejecucion

Instrucciones para ejecutar el proyecto en un ambiente local:

1. Clonar el repositorio
2. Ir a la carpeta de posts.
3. Crear un entorno virtual con `pipenv install`. Installar pipenv si no lo tiene con `pip install pipenv`.
4. Activar el entorno virtual con `pipenv shell`.
5. Correr el proyecto: `FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3001`.

Instrucciones para correr el proyecto con Docker:

1. Clonar el repositorio
2. Ir a la carpeta de posts.
3. Crear la imagen de docker con `docker build -t posts .`.
4. Correr el contenedor con `docker run -p 3001:3001 posts`.

## Ejecutar Pruebas con Postman

Para probar el servicio API de posts expuesta, hemos proporcionado una lista de colecciones de Postman que puedes ejecutar localmente descargando cada archivo JSON de colección e importándolo en Postman.

Lista de colecciones de Postman para cada entrega del proyecto:

1. Entrega 1: https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

Después de descargar la colección que deseas usar, impórtala en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/836f6199-9343-447a-9bce-23d8c07d0338" alt="Screenshot" width="800">

Una vez importada la colección, actualiza las variables de colección que especifican la URL donde se está ejecutando cada microservicio.

Para ejecutar la colección de la carpeta posts, primero debe ejecutar la prueba "Creación de usuarios" de la carpeta "Users" y posteriormente ejecutar la prueba "Generación de token" de la carpeta "Users"; si estas dos pruebas salieron satisfactorias podrá ejecutar todas las pruebas de la carpeta "Offers" ya sea una por una o dando clic derecho en la carpeta, en la opción "Run folder".


## Pruebas Unitarias

Para correr las pruebas unitarias, ejecute el siguiente comando en el folder de posts:

`pytest --cov-fail-under=70 --cov=src --cov-report=html`


## Autor

Fernando Garzon; of.garzon2662@uniandes.edu.co
