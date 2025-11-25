# Backend Django con API Rest
Código backend para el gestor de Calificaciones tributarias de NUAM. Integrado en conjunto con el frontend hecho con React.

## Pre-requisitos 
Antes de empezar, asegurarse que su sistema tenga las siguientes tecnologías instaladas:

Requisito | Version | Propósito
:------- | :------- | :-------
Python | 3.12+ | Entorno de ejecución
MySQL Server | 5.7+ o 8.0+ | Servidor de Base de datos
pip | Última versión | Gestor de paquetes de Python
git | Última versión | Control de versiones

Para más información, revisar el archivo [settings](https://github.com/valen-tina85/Backend-Django-Rest-Framework/blob/14889e46/calificaciones/settings.py) del proyecto.

## Descripción del proceso de configuración
### Paso 1: Clonar repositorio y crear el entorno virtual de ejecución
```
# Clonar el repositorio
git clone https://github.com/valen-tina85/Backend-Django-Rest-Framework.git
cd Backend-Django-Rest-Framework

# Crear el entorno virtual de ejecución
python -m venv venv

# Activar el entorno
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```
### Paso 2: Instalar las dependencias requeridas
El proyecto requiere de los siguientes paquetes de Python:
```
pip install django==5.2.7
pip install djangorestframework
pip install django-cors-headers
pip install mysqlclient
pip install django-filter
```
### Paquetes requeridos
Paquete | Propósito 
:------- | :-------
django | Framework web
djangorestframework | Rest API Framework
django-cors-headers	| Soporte para Cross-origin
mysqlclient | Adaptador para MySQL
django-filter | Filtro de búsqueda

Para más información, revisar el archivo "settings.py" del proyecto.

### Paso 3: Configurar la base de datos MySQL
### Crear la base de datos
Acceder a MySQL y crear la base de datos requerida:
```
mysql -u root -p

CREATE DATABASE nuam_calificaciones CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### Parámetros de configuración de la base de datos

Parámetro | Valor por defecto | Descripción
:------- | :------- | :-------
ENGINE | django.db.backends.mysql	| Base de datos Backend
NAME | nuam_calificaciones | Nombre de la BD
HOST | 127.0.0.1 | Dirección del servidor de la BD
PORT | 3306 | Puerto de conexión de MySQL
USER | root | Usuario de la BD
PASSWORD | Sin contraseña | Contraseña del usuario

### Personalizar la configuración de la BD
Para mayor seguridad con respecto a los datos, se recomienda siempre utilizar en producción un usuario diferente a `root`, además de configurar al usuario con una contraseña 
y permisos restringidos. Teniendo en cuenta esto, para personalizar la configuración de la BD se debe editar desde el archivo `calificaciones/settings.py`:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nuam_calificaciones',
        'HOST': '127.0.0.1',              # Actualizar
        'PORT': '3306',                # Actualizar
        'USER': 'usuario_mysql',      # Actualizar 
        'PASSWORD': 'contraseña_usuario',     # Actualizar
    }
}
```

### Paso 4: Ejecutar la migración de la BD
Aplicar el esquema inicial de la BD definido en [Migraciones](https://github.com/valen-tina85/Backend-Django-Rest-Framework/blob/14889e46/datos/migrations/0001_initial.py#L1-L20)
```
python manage.py migrate
```
Esto creará las 3 tablas principales del proyecto: Mercado, Origen y Calificación.
Se espera el siguiente output en consola:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, datos, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  ...
  Applying datos.0001_initial... OK
```

### Paso 5: Iniciar el servidor de desarrollo
Para iniciar el servidor de desarrollo de Django:
```
python manage.py runserver
```

## API Endpoints
La API de las Calificaciones se exponen a través de la clase `OrigenViewSet`, que amplía `ModelViewSet` de Django REST Framework. Esto proporciona un conjunto completo de operaciones CRUD a través de métodos HTTP RESTful en la URL base /datos/origenes/.

Método HTTP | Endpoint | Acción ViewSet | Propósito
:------- | :------- | :------- | :-------
GET | /datos/calificaciones/ | list() | Obtiene todas las calificaciones
POST | /datos/calificaciones/ | create() | Crea una nueva calificación
GET | /datos/calificaciones/{id}/ | retrieve() | Obtiene una calificación por ID
PUT | /datos/calificaciones/{id}/ | update() | Actualización total de una calificación
PATCH | /datos/calificaciones/{id}/ | partial_update() | Actualización parcial de una calificación
DELETE | /datos/calificaciones/{id}/ | destroy() | Elimina una calificación





