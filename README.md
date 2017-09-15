En cada carpeta se encuentra lo necesario para construir cada contenedor. 
Esto es el fichero dockerfile.

Para arrancar los disntitos contenedores con Docker, si no están arrancados ya, teclear

- docker-compose up

Para visualizar la informacion en Kibana realizar el SSH enlazando el puerto 5601 del iaas
con el tuyo local 

- ssh -L5601:localhost:5601 user@vituin.iaas.ull.es

