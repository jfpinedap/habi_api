# Summary
This API provides two microservices, the first allows users to obtain properties from the database by applying filters by year of construction, city and status. The second allows users to bookmark properties.

# Habi Code Challenge

Esta API dispone de dos microservicios, el primero permite a los usuarios obtener los inmuebles que están en la base de datos aplicando filtros por año de construcción, ciudad y estado. El segundo permite a los usuarios etiquetar los inmuebles como favoritos.

La primera cuestión fue determinar cuál framework y que herramientas utilizar. Personalmente prefiero utilizar Django básicamente por su equilibrio entre Seguridad y Desempeño. La estrategia inicial es utilizar docker-compose para facilitar labores de despliegue del ambiente desarrollo local y que permitirá fácilmente extender a los ambientes de desarrollo, QA y producción. Luego de tener la plantilla se deberá replicar la base de datos en mi local a través de las migraciones de Django creadas a partir de los modelos, una vez se tienen los modelos que corresponden a la base de datos existente se creará un manager para personalizar la consulta que estará soportada por una query en SQL directamente a la base de datos y que dará como resultado la respuesta filtrada que se pide para el primer microservicio. Este proceso de creación de la consulta comienza con el diseño de las pruebas con su respectivos datos de prueba y datos esperados de salida que evaluará los modelos y los diferentes posibles casos de combinación de filtros año de construcción, ciudad y estado. Teniendo estos datos de entrada y salida se puede trabajar en el manager que resolverá el problema. Se utilizará nose para hacer testing y como extra se utilizará redis para tener caché de las consultas realizadas con el fin de mejorar la experiencia del usuario.

# Project Structure

Se configura la estructura del proyecto utilizando **docker-compose**: Acá tuve mi primer demora dado que nunca había configurado MySQL para Django y realmente el inconveniente estuvo en encontrar las dependencias para python:3.8.3-alpine ya lo demás fue más sencillo.

# Models and Test configuration

Se realiza la configuración de los modelos para que coincida con la base de datos. Además se genera un datos de prueba tanto de entrada como de salida para dar paso al desarrollo del manager quien hará los filtros necesarios.
En esta etepa también se decide que la consulta se recibirá empleando el mátodo GET-REST pasando los valores por la url de la sigiente forma `domain/property?city=<str>&year=<str>&status=<str>`
