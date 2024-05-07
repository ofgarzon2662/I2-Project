# Desarrollo App Nube Nativa - Grupo 5

Proyecto del curso desarrollo de aplicaciones nativas en la nube - MISO

## Índice

1. [Estructura](#estructura)
2. [Ejecución](#ejecución)
3. [Pruebas](#pruebas)
4. [Autor](#autor)

## Estructura

### Carpetas:
- `.github `: Pipelines de la aplicación
- `Users `: código de la aplicación Users - README.md # revisar para más detalles
- `Routes `: código de la aplicación Routes - README.md # revisar para más detalles
- `Post `: código de la aplicación Post - README.md # revisar para más detalles
- `Offers `: código de la aplicación Offers - README.md # revisar para más detalles
- `Users `: código de la aplicación Users - README.md # revisar para más detalles
- `Users `: código de la aplicación Users - README.md # revisar para más detalles
### Archivos:
- `Config.yaml `: Archivo que contiene la configuración para ejecutar las pruebas con pipeline de la entrega 1 
- `docker-compose.yml `: Archivo para correr las aplicaciones contenerizadas

## Ejecución
Para ejecutar se debe abrir el CMD desde la raíz del proyecto clonado y ejecutar el comando `docker-compose up`

## Pruebas

Para probar los servicios API expuestos por cada microservicio, hemos proporcionado una lista de colecciones de Postman que puedes ejecutar localmente descargando cada archivo JSON de colección e importándolo en Postman.

Lista de colecciones de Postman para cada entrega del proyecto:
- https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

Después de descargar la colección que deseas usar, impórtala en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/836f6199-9343-447a-9bce-23d8c07d0338" alt="Screenshot" width="800">

Una vez importada la colección, actualiza las variables de colección que especifican la URL donde se está ejecutando cada microservicio.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/efafbb3d-5938-4bd8-bfc7-6becfccd2682" alt="Screenshot" width="800">

Finalmente, ejecuta la colección haciendo clic derecho en su nombre y haciendo clic en el botón "Run collection", esto ejecutará múltiples solicitudes API y también ejecutará algunos assertions que hemos preparado para asegurarnos de que el microservicio esté funcionando como se espera.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/f5ca6f7c-e4f4-4209-a949-dcf3a6dab9e3" alt="Screenshot" width="800">

## Autor

Grupo 5:
1. Johanna Beltran
2. Alejandro Martinez
3. Fernando Garzon
4. Esteban Reyes
