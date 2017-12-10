# django-docker-semestral
Proyecto semestral de Django con Docker Compose

## Prerequisitos
Instalar docker, docker-compose. Para saber más, ir [aquí.](https://www.docker.com/what-docker)

## Instalar dependencias para el proyecto
```
# Instalar fuera del docker, pip:
sudo apt-get install python-pip

# Instalar virtualenv
sudo pip install virtualenv

# Crear entorno virtual (Se ejecuta desde la misma carpeta del proeyecto, donde está el "docker-compose.yml")
virtualenv venv

# Activar entorno virtual (Se ejecuta desde la misma carpeta del proeyecto, donde está el "docker-compose.yml")
source venv/bin/activate

# Instalar django en el entorno virtual
pip install django

# Desactivar entorno virtual cuando se terminó de trabajar
deactivate
```

## Crear nueva app de Django
### Todos los comandos deben ser ejecutados desde la carpeta donde se encuentra el docker-compose.yml y debe haber estado el django instalado previamente
```
# Activar entorno virtual
source venv/bin/activate

# Ir a la carpeta donde se quiere crear el app
cd <carpeta>

# Crear app
django-admin startapp <nombre_del_app>
```

## Crear super usuario 
### Todos los comandos deben ser ejecutados desde la carpeta donde se encuentra el docker-compose.yml y el docker-compose debe estar abierto en otro terminal o demonizado.
```
# Averiguar el proceso del contenedor de docker
docker ps

# Usar el "CONTAINER_ID" de la tabla anterior, para ejecutar:
docker exec -it <CONTAINER_ID_DEL_CONTENEDOR_DE_DJANGO> bash

# Crear el super usuario
python manage.py createsupuser

# Salir del contenedor
exit
```

## Entrar al "shell" de python del contenedor
### Todos los comandos deben ser ejecutados desde la carpeta donde se encuentra el docker-compose.yml y el docker-compose debe estar abierto en otro terminal o demonizado.
```
# Averiguar el proceso del contenedor de docker
docker ps

# Usar el "CONTAINER_ID" de la tabla anterior, para ejecutar:
docker exec -it <CONTAINER_ID_DEL_CONTENEDOR_DE_DJANGO> bash

# Crear el super usuario
python manage.py shell

# Salir del shell
>>> exit()  # Sin el ">>>"

# Salir del contenedor
exit
```

## Detener todos los procesos de docker
```
docker stop $(docker ps -a -q)
```