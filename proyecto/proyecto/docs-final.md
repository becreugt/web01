# Preparar el proyecto
## Generar dependencias
```
uv pip compile pyproject.toml -o requirements.txt
```

## Modificar los settings
```
# Agregar
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Modificar
ALLOWED_HOSTS = ['usuario.pythonanywhere.com']
```

# Preparación GitHub
1. Crear la cuenta
2. Crear el repositorio con nombre "web01" (con .gitignore de Python)
3. Subir el código. Revisar de no subir la base de datos ni el .venv

# Creación cuenta Python Anywhere
1. Crear la cuenta
2. Validar la cuenta

## Acceso a consola de Python Anywhere

1. Click en Consoles
2. Click en Bash

## Configurar la conexión a GitHub

Generar la clave en el servidor

```
ssh-keygen
cat ~/.ssh/id_rsa.pub
```

Copiar el contenido de la clave.

Agregar la clave en GitHub

1. En el repositorio ir a Settings
2. Click en Deploy Keys
3. Click en Add Deploy Key
4. Pegar el contenido de la clave

De regreso en la consola de Python Anywhere>

```
git clone https://github.com/usuario/web01.git
cd web01
```

# Instalar el codigo

Crear un ambiente de ejecucion:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Preparar los valores de Django

```
cd proyecto
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

# Configurar la aplicacion

1. Ir a la pestaña Web en el menú superior de PythonAnywhere
2. Click en Add a new web app
3. Elegir Manual Configuration
4. Seleccionar la version de Python

Ahora, en la sección de rutas

- El código está en `/home/usuario/web01/proyecto`
- El ambiente virtual está en `/home/usuario/web01/.venv`


# Preparar el servidor

En la pestaña Web, dentro de la sección Code, click en el enlace al archivo de configuración WSGI.

Remplazar el contenido con esto

```
import os
import sys

path = '/home/jinchuika/web01/proyecto'
if path not in sys.path:
    sys.path.append(path)

# Configurar la variable de entorno para los settings de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'proyecto.settings'

# Levantar la aplicación WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
