# Listado de ejercicios

## Parte 1: Despliegue de imágenes simples

En los siguientes ejercicios se le pedirá descargar, configurar y levantar imágenes oficiales de Dockerhub y así, rápidamente tener acceso a ciertas aplicaciones.

1. Utilizando el cliente en consola de docker, descargue y levante un contenedor con la imagen [hello-world](https://hub.docker.com/_/hello-world)
2. Cree un `Dockerfile` y un `docker-compose.yaml`  para levantar una instancia de `mongo` utilizando la imágen oficial. Para ello, puede consultar la siguiente [documentación](https://hub.docker.com/_/mongo) ya que tendrá que agregar algunas variables de ambiente para acceder al servidor de mongo.
3. Como continuación del ejercicio anterior, agregue un volumen desde su `docker-compose.yaml` de manera que los datos persistan cuando elimine los contenedores.
4. Cree una pequeña aplicación en python (puede ser una aplicación de consola o un web server) que inserte cualquier información en una colleción de mongo que deplegó en los pasos anteriores. Considere agregar el respectivo Dockerfile y servicio en su archivo `docker-compose.yaml`. Utilice cualquier imagen igual o superior a 3.10 de python.
5. Modifique su imágen del paso 4 y agregue en su lógica una variable de ambiente llamada `STATE`. Si `STATE` es igual a INSERT, mantenga su lógica actual de insertar datos en la base de datos de mongo. Por otro lado si el valor equivale a `READ`, lea todas los datos disponibles de la base de datos en mongo y muentrelos en consola.

## Parte 2: Despliegue de aplicaciones existentes

1. Clone el siguiente repositorio [repositorio](https://github.com/talkpython/web-applications-with-fastapi-course). Este es un repositorio público con algunas aplicaciones de ejemplos utilizando la biblioteca de FastAPI. Navegue al directorio code/ch6-users-and-forms. Su tarea es desplegar esta aplicación utilizando contenedores de Docker. Examine la aplicación, puertos y cualquier otra configuración necesaria para crear un Dockerfile y contruir una imagen. Una vez hecho, corra (comando `run`) dicha imágen.
2. Clone el siguiente [repositorio](https://github.com/ShaunZA/flask-riddle-game). La aplicacion corresponde a un juego de [riddle](https://shaun-riddle-game.herokuapp.com/hey/game) utilizando python y FlaskAPI. Su tarea es desplegar esta aplicación utilizando contenedores de Docker. Examine la aplicación, puertos y cualquier otra configuración necesaria para crear un Dockerfile y contruir una imagen. Una vez hecho, corra (comando `run`) dicha imágen.