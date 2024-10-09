# Generalidades

Evidentemente este proyecto se puede realizar de infinitas maneras diferentes. Decidí utilizar las siguientes herramientas

- fastapi
- reactjs
- ECS
- dynamoDB
- AWS CDK y CloudFormation tras bambalinas

> Las imágenes tanto del backend como el frontend fueron subidas a [docker.hub](https://hub.docker.com/repository/docker/jhonsanz/amaris-prueba/general)

# Consideraciones del backend con fastApi

Debido a la utilización de fastApi se incurre en gastos de utilización de los servicios de cloud computing de AWS como EC2 o Fargate. Si bien para este proyecto utilizar fastApi **es como matar una mosca con una escopeta**, decidí hacerlo así para mostrar un poco de mi manejo de contenedores, ya que el objetivo de la prueba es mostrar mis habilidades desarrollo.

Como se mencionó al inicio, es claro que el backend se puede realizar con **funciones lambda**, pero la descripción de la prueba me daba cierta libertad en el uso de las herramientas, y esta se limitaba solo a utilizar python. De todos modos, el hacerlo con funciones lambda es muy similar, ya que esto realmente se trata de comunicarnos a dynamoDB

# 