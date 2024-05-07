# Routes

El servicio de gestión de trayectos permite crear trayectos (rutas) para ser usados por las publicaciones.

## Índice

1. [Estructura](#estructura)
2. [Ejecución](#ejecución)
3. [Autor](#autor)

## Estructura

El microservicio utiliza Python y Flask para ejecutar el servidor, y pytest para ejecutar las pruebas unitarias. En general hay dos carpetas principales: `src` y `tests`, así como algunos archivos de soporte.

### Archivos de soporte
- `Pipfile`: Este archivo declara todas las dependencias que serán utilizadas por el microservicio. Consulta la sección **Instalar dependencias**.
- `.env.template`: Archivo de plantilla Env utilizado para definir variables de entorno. Consulte la sección  **Variables de entorno**.
- `.env.test`: Archivo utilizado para definir variables de entorno para las pruebas unitarias. Consulta la sección **Variables de entorno**.
- Dockerfile: Definición para construir la imagen Docker del microservicio. Consulta la sección **Ejecutar desde Dockerfile**.

### Carpeta src
Esta carpeta contiene el código y la lógica necesarios para declarar y ejecutar la API del microservicio, así como para la comunicación con la base de datos. Hay 4 carpetas principales:
- `/models`: Esta carpeta contiene la capa de persistencia, donde se declaran los modelos que se van a persistir en la base de datos en forma de tablas, así como la definición de cada columna. 
- `/commands`: Esta carpeta contiene cada caso de uso que estamos implementando en nuestro microservicio, es decir, la lógica del negocio siguiendo un patrón de diseño de comandos. Para cada caso de uso (como crear un trayecto, obtener un trayecto, etc.) tendremos un archivo separado. Cada comando heredará una clase `BaseCommand` que ya está proporcionada en el archivo `/commands/base_command.py` e implementará el método `execute`. Este método es el que contendrá la lógica del negocio.
- `/blueprints`: Esta carpeta contiene la capa de aplicación de nuestro microservicio, responsable de declarar cada servicio API que estamos exponiendo, así como su implementación. 
- `/errors`: Para devolver errores HTTP en los blueprints, utilizamos clases de excepción personalizadas que declaran qué mensaje y qué código HTTP retornar cuando ocurre esa excepción. Estas excepciones se declaran dentro del archivo `/errors/errors.py`, donde se proporciona una clase base `ApiError`. 

### Carpeta test
Esta carpeta contiene las pruebas para los componentes principales del microservicio que han sido declarados en la carpeta `/src`


## Ejecución
### Instalar dependencias
Utilizamos pipenv para gestionar las dependencias (verificar la sección de requisitos previos) y las declaramos todas dentro del archivo Pipfile del microservicio. Antes de instalar las dependencias, inicia el shell de pipenv para activar el entorno virtual con el siguiente comando:

```bash
$> pipenv shell
``` 
Luego ejecuta el comando de instalación.
```bash
$> pipenv install
```
Esto instalará las dependencias solo dentro del entorno virtual, así que recuerda activarlo cuando estés trabajando con el microservicio. Para obtener más información sobre pipenv, consulta la documentación oficial en https://pipenv-es.readthedocs.io.

Para salir del entorno virtual, utiliza el siguiente comando:
```bash
$> deactivate
```

### Variables de entorno

El servidor Flask y las pruebas unitarias utilizan variables de entorno para configurar las credenciales de la base de datos y encontrar algunas configuraciones adicionales en tiempo de ejecución. A alto nivel, esas variables son:
- DB_USER: Usuario de la base de datos Postgres
- DB_PASSWORD: Contraseña de la base de datos Postgres
- DB_HOST: Host de la base de datos Postgres
- DB_PORT: Puerto de la base de datos Postgres
- DB_NAME: Nombre de la base de datos Postgres
- USERS_PATH: Variable de entorno que contiene la URL utilizada para acceder a los endpoints de usuarios

Estas variables de entorno estan especificadas en `.env.development` y `.env.test`. 

### Ejecutar el servidor
Una vez que las variables de entorno estén configuradas correctamente, para ejecutar el servidor utiliza el siguiente comando:
```bash
# Routes
$> pipenv run flask -A src/main.py run -p 3002
```
### Ejecutar pruebas
Para ejecutar las pruebas unitarias, ejecuta el siguiente comando:
```bash
pytest --cov-fail-under=70 --cov=src
pytest --cov-fail-under=70 --cov=src --cov-report=html
```
### Ejecutar desde Dockerfile
Para construir la imagen del Dockerfile en la carpeta, ejecuta el siguiente comando:
```bash
$> docker build . -t <NOMBRE_DE_LA_IMAGEN>
```
Y para ejecutar esta imagen construida, utiliza el siguiente comando:
```bash
$> docker run <NOMBRE_DE_LA_IMAGEN>
```

### Ejecutar Colección de Postman
Para probar los servicios API expuestos por Routes, hemos proporcionado una lista de colecciones de Postman que puedes ejecutar localmente descargando cada archivo JSON de colección e importándolo en Postman.

Lista de colecciones de Postman:
- https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

Después de descargar la colección que deseas usar, impórtala en Postman utilizando el botón Import en la sección superior izquierda.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/836f6199-9343-447a-9bce-23d8c07d0338" alt="Screenshot" width="800">

Una vez importada la colección, actualiza las variables de colección que especifican la URL donde se está ejecutando cada microservicio.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/efafbb3d-5938-4bd8-bfc7-6becfccd2682" alt="Screenshot" width="800">

Finalmente, ejecuta la colección Users primero y luego Routes haciendo clic derecho en su nombre y haciendo clic en el botón "Run collection", esto ejecutará múltiples solicitudes API y también ejecutará algunos assertions que hemos preparado para asegurarnos de que el microservicio esté funcionando como se espera.

<img src="https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-base/assets/78829363/f5ca6f7c-e4f4-4209-a949-dcf3a6dab9e3" alt="Screenshot" width="800">

## Autor

Esteban Reyes Marcelo
