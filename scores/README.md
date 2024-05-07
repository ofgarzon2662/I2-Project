# Offers

## Pre-requisitos para cada microservicio
- Python ~3.9
- Docker
- Docker-compose
- Postman
- PostgreSQL

## Ejecutar un microservicio
Se debe ejecutar el siguiente comando desde la raíz del proyecto: docker-compose up
Una vez finalice de ejecutar se podrá probar el servicio desde Postman como se describe a continuación.

## Ejecutar Colección de Postman
Para probar el servicio API de usuarios expuesta, hemos proporcionado una lista de colecciones de Postman que puedes ejecutar localmente descargando cada archivo JSON de colección e importándolo en Postman.

Lista de colecciones de Postman para cada entrega del proyecto:
- Entrega 2: https://teams.microsoft.com/l/message/19:meeting_OGFiNDgyOWQtZDA1Yi00YTAzLWJiZGYtMjY2MDkyOThjZDk3@thread.v2/1709395683514?context=%7B%22contextType%22%3A%22chat%22%7D

Después de descargar la colección que deseas usar, impórtala en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/836f6199-9343-447a-9bce-23d8c07d0338" alt="Screenshot" width="800">

Una vez importada la colección, actualiza las variables de colección que especifican la URL donde se está ejecutando cada microservicio.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/efafbb3d-5938-4bd8-bfc7-6becfccd2682" alt="Screenshot" width="800">

Podrá ejecutar todas las pruebas de la carpeta "Users" ya sea una por una o dando clic derecho en la carpeta, en la opción "Run folder"