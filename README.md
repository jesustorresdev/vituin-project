En cada carpeta se encuentra lo necesario para construir cada contenedor. 
Esto es el fichero dockerfile.

Para arrancar los disntitos contenedores con Docker, si no están arrancados ya, teclear

- docker-compose up

Para visualizar la informacion en Kibana realizar el SSH enlazando el puerto 5601 del iaas
con el tuyo local :

- ssh -L5601:localhost:5601 user@vituin.iaas.ull.es

También puedes acceder a Elasticsearch mediante el puerto 9200 haciendo el túnel:

- ssh -L9200:localhost:9200 user@vituin.iaas.ull.es

Y a airflow por el 8080:

- ssh -L8080:localhost:8080 user@vituin.iaas.ull.es
