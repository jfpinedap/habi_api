# Summary
This API provides two microservices, the first allows users to obtain properties from the database by applying filters by year of construction, city and status. The second allows users to bookmark properties.

# Habi Code Challenge

Me voy a permitir discutir la estrategia de solución, la descripción de problemas y su solución en español para lo demás se utilizará inglés.

Esta API dispone de dos microservicios, el primero permite a los usuarios obtener los inmuebles que están en la base de datos aplicando filtros por año de construcción, ciudad y estado. El segundo permite a los usuarios etiquetar los inmuebles como favoritos.

La primera duda fue determinar cuál framework y que herramientas utilizar. Personalmente prefiero utilizar Django básicamente por su equilibrio entre Seguridad y Desempeño. La estrategia inicial es utilizar **docker-compose** para facilitar labores de despliegue del ambiente desarrollo local y que permitirá fácilmente extender a los ambientes de desarrollo, QA y producción. Luego de tener la plantilla se deberá replicar la base de datos en mi local a través de las migraciones de **Django** creadas a partir de los modelos, una vez se tienen los modelos que corresponden a la base de datos existente se creará un manager para personalizar la consulta que estará soportada por una query en SQL directamente a la base de datos y que dará como resultado la respuesta filtrada que se pide para el primer microservicio. Este proceso de creación de la consulta comienza con el diseño de las pruebas con su respectivos datos de prueba y datos esperados de salida que evaluará los modelos y los diferentes posibles casos de combinación de filtros para el año de construcción, ciudad y estado. Teniendo estos datos de entrada y salida se puede trabajar en el manager que resolverá el problema. Se utilizará **nose** para hacer testing y como adicional se utilizará **redis** para soportar el caché de las consultas realizadas por dos minutos con el fin de mejorar la experiencia de usuario además de  reducir el procesamiento en la DB y el tráfico de su petición.

# Project Structure

Se configura la estructura del proyecto utilizando **docker-compose**: Acá tuve una demora, no había configurado MySQL para Django y el inconveniente estuvo en encontrar las dependencias para **python:3.8.3-alpine** ya lo demás fue más sencillo.

# Models and Test configuration

Se realiza la configuración de los modelos para que coincida con la base de datos. Además se generan datos de prueba, tanto de entrada como de salida, para dar paso al desarrollo del manager que hará los filtros a petición del usuario.
En esta etepa también se decide que la consulta se recibirá empleando el método GET-REST pasando los valores por la url de la sigiente forma `domain/property?city=<str>&year=<str>&status=<str>`


# Property Manager development
Tuve problemas con el versionamiento de las bases de datos en **MySQL 8.0** están disponibles las instrucciones **ROW_NUMBER()** y **WITH AS**. Las emplee en el desarrollo local pero cuando las probé contra la base de datos de la nube no funcionaba, así que reescribí la consulta para **MySQL 5.7** y todo funcionó según lo esperado junto con el testing. Esta es una mejora que se puede hacer a las bade de datos, actualizarla a la version 8.0, en mi local trabaja más rápido que en la nube y eso no sé porque pasa. :\

#  Entity Relationship Model - Properties favorites with owner

La solución que propongo es una típica relación many to many que emplea una Through Table para hacer de puente entre la relación del usuario y el inmueble dejando un timestamp de cuando efectua el like. A continuación el modelo propuesto:

![Modelo](/images/entity_relationship_model.png?style=centerme)


## Requirements

* Git
* Docker
* Docker-compose
* .local → .envs/.local | File with local environment variables **provided by email**
## How to use this project

* Clone this repository
  ```sh
  git clone https://github.com/jfpinedap/habi_api.git
  cd habi_api
  ```

* Copy .local file in .envs folder

* Build the Dockerfile
  ```sh
  docker-compose up --build -d
  ```

* Request localy by port 8000 in a browser or using Postman, examples:
  ```sh
  http://0.0.0.0:8000/property
  ```
  ```sh
  http://0.0.0.0:8000/property?city=bogota&year=2000
  ```

* Testing
  ```sh
  docker-compose run --rm django python manage.py test
  ```

## Used technologies

* Django
* Django Rest Framework
* Redis
* [Docker](https://www.docker.com/ "Docker link")
* Docker-compose

## Licence

GNU-GPL 3.0
