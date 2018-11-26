# Makefile

start:
	docker-compose up -d $(c)

stop:
	docker-compose down $(c)

build:
	docker-compose build $(c)

status:
	docker-compose ps

ps: status

shell:
	test -n "$(c)"  # $$c=container
	docker exec -it $(c) bash

shell-airflow:
	docker exec -it --entrypoint bash airflow

check-network-config-details:
	docker network inspect vituinproject_default

update:
	test -n "$(c)"  # $$c=container
	docker-compose up -d --no-deps --build $(c)
